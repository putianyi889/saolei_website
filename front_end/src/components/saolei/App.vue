<template>
    <Main v-if="state === 'main'" @enter-auto="state = 'auto'" @enter-page="state = 'page'" @enter-queue="state = 'queue'" />
    <ImportAll v-if="state === 'auto'" :user-id="store.user.id" @back="state = 'main'" />
    <PageImport v-if="state === 'page'" :saolei-id="saoleiId" @back="state = 'main'" @enter-queue="state = 'queue'" />
    <VideoImportQueue v-if="state === 'queue'" :saolei-id="saoleiId" @back="state = 'main'" />
</template>

<script setup lang="ts">
import { defineAsyncComponent, ref } from 'vue';

import { store } from '@/store';

const Main = defineAsyncComponent(() => import('./Main.vue'));
const ImportAll = defineAsyncComponent(() => import('./ImportAll.vue'));
const PageImport = defineAsyncComponent(() => import('./PageImport.vue'));
const VideoImportQueue = defineAsyncComponent(() => import('./VideoImportQueue.vue'));

defineProps({
    saoleiId: {
        type: Number,
        required: true,
    },
});

const state = ref('main');
</script>
