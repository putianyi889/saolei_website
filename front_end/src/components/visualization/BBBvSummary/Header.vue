<template>
    <el-row>
        <el-select v-model="BBBvSummaryConfig.template" size="small" style="width: 80px">
            <el-option :label="t('common.prop.bvs')" value="bvs" />
            <el-option :label="t('common.prop.time')" value="time" />
            <el-option :label="t('common.prop.stnb')" value="stnb" />
            <el-option :label="t('common.prop.ioe')" value="ioe" />
            <el-option :label="t('common.prop.thrp')" value="thrp" />
            <el-option :label="t('BBBvSummary.customTemplate')" value="custom" />
        </el-select>
        &nbsp;
        <SoftwareFilter v-model="BBBvSummaryConfig.softwareFilter" />
        <span style="flex: 1" />
        <base-tooltip follow-cursor>
            <el-link
                :underline="false"
                @click="BBBvSummaryConfig.tooltipMode === 'fast' ? BBBvSummaryConfig.tooltipMode = 'advanced' : BBBvSummaryConfig.tooltipMode = 'fast'"
            >
                {{ t(`BBBvSummary.tooltipMode.${BBBvSummaryConfig.tooltipMode}`) }}
            </el-link>
            <template #content>
                {{ t(`BBBvSummary.tooltipMode.${BBBvSummaryConfig.tooltipMode}Tooltip`) }}
            </template>
        </base-tooltip>
        &nbsp;
        <Zoomer v-model="BBBvSummaryConfig.zoom" />
    </el-row>
    <el-row v-if="BBBvSummaryConfig.template === 'custom'" style="margin-top: 5px;">
        <el-link :underline="false" @click="BBBvSummaryConfig.sortDesc = !BBBvSummaryConfig.sortDesc">
            {{ BBBvSummaryConfig.sortDesc ? t('BBBvSummary.settingMax') : t('BBBvSummary.settingMin') }}
        </el-link>
        &nbsp;
        <el-select v-model="BBBvSummaryConfig.sortBy" size="small" style="width:65px;">
            <el-option :label="t('common.prop.time')" value="timems" />
            <el-option :label="t('common.prop.ioe')" value="ioe" />
            <el-option :label="t('common.prop.thrp')" value="thrp" />
        </el-select>
        &nbsp;
        <el-text>{{ t('BBBvSummary.settingDisplayBy') }}</el-text>
        &nbsp;
        <el-select v-model="BBBvSummaryConfig.displayBy" size="small" style="width:70px;">
            <el-option :label="t('common.prop.bvs')" value="bvs" />
            <el-option :label="t('common.prop.time')" value="time" />
            <el-option :label="t('common.prop.stnb')" value="stnb" />
            <el-option :label="t('common.prop.ioe')" value="ioe" />
            <el-option :label="t('common.prop.thrp')" value="thrp" />
        </el-select>
    </el-row>
</template>

<script setup lang="ts">

import { ElRow, ElSelect, ElOption, ElLink, ElText } from 'element-plus';
import { BBBvSummaryConfig } from '@/store';
import { useI18n } from 'vue-i18n';
import SoftwareFilter from '@/components/Filters/SoftwareFilter.vue';
import Zoomer from '@/components/widgets/Zoomer.vue';
import BaseTooltip from '@/components/common/BaseTooltip.vue';

const { t } = useI18n();

</script>
