<template>
    <iframe :src="`http://saolei.wang/Video/My.asp?Id=${saoleiId}&Order=Time&Page=${page}`" style="width: 580px; height: 560px; pointer-events: none;" />
</template>

<script setup lang="ts">

defineProps({
    saoleiId: {
        type: Number,
        required: true,
    },
    page: {
        type: Number,
        default: 1,
    },
});

</script>
