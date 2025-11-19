<template>
    <base-button-back @click="$emit('back')" />
    从第
    <el-input-number v-model="startPage" :min="1" :max="endPage" :disabled="running" />
    页到第
    <el-input-number v-model="endPage" :min="startPage" :disabled="running" />
    页
    <el-button :disabled="running" @click="importAll">
        开始
    </el-button>
    <el-button v-if="running" :disabled="stopping" @click="fullLog.terminate();">
        终止
    </el-button>
    <el-button @click="console.log(fullLog)">调试</el-button>
    <el-carousel v-if="!ArrayUtils.isEmpty(fullLog.pageLogs)" :autoplay="false" trigger="click" :initial-index="fullLog.pageIndex" type="card" :loop="false" height="15rem">
        <el-carousel-item v-for="pageLog of fullLog.pageLogs" :key="pageLog.index" :name="pageLog.index.toString()">
            <base-card-normal style="height: 100%; overflow-y: auto;">
                <h3 v-if="pageLog.state === 'empty'" class="justify-center small" text="2xl">
                    第{{ pageLog.index }}页无录像可导入
                </h3>
                <PageLogView v-if="pageLog.state !== 'empty'" :data="pageLog" />
            </base-card-normal>
        </el-carousel-item>
    </el-carousel>
</template>

<script setup lang="ts">
import { ElButton, ElCarousel, ElCarouselItem, ElInputNumber } from 'element-plus';
import { ref } from 'vue';
import { useI18n } from 'vue-i18n';

import { ImportLog } from './importLog';
import PageLogView from './PageLogView.vue';

import BaseButtonBack from '@/components/common/BaseButtonBack.vue';
import { sleep } from '@/utils';
import { ArrayUtils } from '@/utils/arrays';
import useCurrentInstance from '@/utils/common/useCurrentInstance';
import BaseCardNormal from '@/components/common/BaseCardNormal.vue';

const { proxy } = useCurrentInstance();
const { t } = useI18n();

const props = defineProps({
    userId: {
        type: Number,
        required: true,
    },
});

const startPage = ref(1);
const endPage = ref(1000);
const running = ref(false);
const stopping = ref(false);
const fullLog = ref<ImportLog>(new ImportLog());

async function importAll() {
    running.value = true;
    fullLog.value = new ImportLog();
    fullLog.value.startingPage = startPage.value;
    while (!fullLog.value.isFinished()) {
        fullLog.value.newPage();
        const pageLog = fullLog.value.getCurrentPageLog();
        fullLog.value.videoListStart();
        await proxy.$axios.post('accountlink/saolei/importlist/', {
            user_id: props.userId,
            page: fullLog.value.getCurrentPageLog().index,
        }).then((response) => {
            const data = response.data;
            if (data.type === 'success') {
                fullLog.value.videoListFinish(data.data);
            } else {
                fullLog.value.videoListError(data.obj, data.category);
            }
        }).catch((error) => {
            fullLog.value.consoleError(error);
        });
        await sleep(500);
        while (!pageLog.isFinished()) {
            fullLog.value.videoStart();
            const video = fullLog.value.getCurrentVideo();
            await proxy.$axios.post('accountlink/saolei/importvideo/', {
                video_id: video.id,
            }).then((response) => {
                const data = response.data;
                if (data.type === 'success') {
                    fullLog.value.videoSuccess();
                } else {
                    fullLog.value.videoError(data.obj, data.category);
                }
            }).catch((error) => {
                fullLog.value.consoleError(error);
            });
            await sleep(500);
        }
        if (fullLog.value.getCurrentPageLog().index >= endPage.value) {
            fullLog.value.terminate();
        }
    }
    running.value = false;
}

defineEmits(['back']);

</script>
