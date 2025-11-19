<template>
    <el-timeline>
        <el-timeline-item v-for="baseLog of data.videoLogs" :key="baseLog.time.toISOString()" :timestamp="toISODateTimeString(baseLog.time)">
            <el-text v-if="baseLog.type === 'consoleError'">
                发生严重错误！
                <el-button @click="handleConsoleLog(baseLog.error)">
                    输出到控制台
                </el-button>
            </el-text>
            <el-text v-else-if="baseLog.type === 'videoStart'">
                开始导入录像#{{ data.videoList[baseLog.videoIndex!].id }}
            </el-text>
            <el-text v-else-if="baseLog.type === 'videoSuccess'">
                录像#{{ data.videoList[baseLog.videoIndex!].id }}导入完成！
            </el-text>
            <el-text v-else-if="baseLog.type === 'videoError'">
                录像#{{ data.videoList[baseLog.videoIndex!].id }}导入失败！
            </el-text>
            <el-text v-else-if="baseLog.type === 'videoListStart'">
                开始获取第{{ data.index }}页录像列表
            </el-text>
            <el-text v-else-if="baseLog.type === 'videoListFinish'">
                第{{ data.index }}页录像列表获取完成！{{ data.videoList.length }}条录像待导入
            </el-text>
            <el-text v-else-if="baseLog.type === 'videoListError'">
                第{{ data.index }}页录像列表获取失败！
            </el-text>
            <el-text v-else-if="baseLog.type === 'pageEnd'">
                第{{ data.index }}页导入完成！
            </el-text>
        </el-timeline-item>
    </el-timeline>
</template>

<script setup lang="ts">
import { ElButton, ElText, ElTimeline, ElTimelineItem } from 'element-plus';

import { PageLog } from './importLog';
import { toISODateTimeString } from '@/utils/datetime';

defineProps({
    data: {
        type: PageLog,
        required: true,
    },
});

function handleConsoleLog(error: any) {
    console.log(error);
}
</script>
