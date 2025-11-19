<template>
    <base-button-back @click="$emit('back')" />
    <div style="justify-self: center;">
        <div>
            <PageFrame :saolei-id="saoleiId" :page="page" />
        </div>
        <div style="position: absolute; top: 50%; transform: translateY(-50%); width: 580px; display: flex; align-items: center;">
            <el-button size="large" circle class="semitransparent" @click="page -= 1; state = '';">
                <base-icon-prev />
            </el-button>
            <span style="flex: 1" />
            <el-button
                v-if="state === '' || state === 'loading'" :loading="state === 'loading'" size="large" class="semitransparent"
                @click="handleImport"
            >
                同步本页数据
            </el-button>
            <el-result
                v-else-if="state === 'success'" icon="success" :title="`本页数据已同步`"
                :sub-title="`${newCount}个录像已加入队列`" class="semitransparent"
            >
                <template #extra>
                    <el-button @click="handleImport">
                        重新同步
                    </el-button>
                    <el-button type="primary" @click="$emit('enterQueue')">
                        查看队列
                    </el-button>
                </template>
            </el-result>
            <el-result v-else icon="error" title="同步失败" :sub-title="`请重试或联系管理员`" class="semitransparent">
                <template #extra>
                    <el-button @click="handleImport">
                        重新同步
                    </el-button>
                </template>
            </el-result>
            <span style="flex: 1" />
            <el-button
                size="large" circle class="semitransparent" @click="page += 1; state = '';"
            >
                <base-icon-next />
            </el-button>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ElButton, ElResult } from 'element-plus';
import { ref } from 'vue';

import PageFrame from './PageFrame.vue';

import BaseButtonBack from '@/components/common/BaseButtonBack.vue';
import { BaseIconNext, BaseIconPrev } from '@/components/common/icon';
import { httpErrorNotification } from '@/components/Notifications';
import useCurrentInstance from '@/utils/common/useCurrentInstance';

const { proxy } = useCurrentInstance();

defineProps({
    saoleiId: {
        type: Number,
        required: true,
    },
});

const page = ref(1);
const state = ref('');
const newCount = ref(0);

async function handleImport() {
    state.value = 'loading';
    await proxy.$axios.post('accountlink/saolei/importlist/', {
        page: page.value,
    }).then((response) => {
        const data = response.data;
        if (data.type === 'success') {
            state.value = 'success';
            newCount.value = data.data.length;
        } else {
            state.value = 'error';
        }
    }).catch((error) => {
        state.value = 'error';
        httpErrorNotification(error);
    });
}

defineEmits(['back', 'enterQueue']);

</script>

<style lang="less" scoped>
.semitransparent {
    background: rgba(0, 0, 0, 0.5);
    vertical-align: middle;
}
</style>
