<template>
    <!-- message的z索引为2015 -->
    <el-menu class="menu" mode="horizontal" :router="true" :default-active="menu_index" :ellipsis="false"
        menu-trigger="click">
        <el-menu-item index="/" class="logo">
            <el-image class="logo1" :src="logo_1" :fit="'cover'" />
            <el-image v-if="!local.menu_icon" class="logo2" :src="logo_2" :fit="'cover'" />
        </el-menu-item>
        <el-menu-item v-for="item in menu_items" :index="'/' + item.index" class="menuitem">
            <el-tooltip v-if="local.menu_icon" :content="$t(item.content)">
                <el-icon class="menumargin">
                    <component :is="item.icon" class="menuicon" />
                </el-icon>
            </el-tooltip>
            <span v-else style="padding-right: 5px">
                <el-icon>
                    <component :is="item.icon" class="menuicon" />
                </el-icon>{{ $t(item.content) }}
            </span>
        </el-menu-item>
        <div style="flex-grow: 1" />
        <el-menu-item :index="player_url" v-if="store.user.id != 0" @click="store.player = store.user" class="menuitem">
            <el-tooltip v-if="local.menu_icon" :content="store.user.username">
                <el-icon class="menumargin">
                    <User class="menuicon" />
                </el-icon>
            </el-tooltip>
            <span v-else style="padding-right: 5px">
                <el-icon>
                    <User class="menuicon" />
                </el-icon>{{ store.user.username }}
            </span>
        </el-menu-item>
        <el-menu-item index="/settings" style="padding-left: 8px; padding-right: 5px">
            <el-tooltip :content="$t('menu.setting')">
                <el-icon>
                    <Setting class="menuicon" />
                </el-icon>
            </el-tooltip>
        </el-menu-item>
        <LanguagePicker v-show="local.language_show" style="padding-left: 8px; padding-right: 8px;" />
        <Login @login="user_login" @logout="user_logout"></Login>
    </el-menu>
    <div class="common-layout">
        <el-container>
            <div class="header_all" style="padding-top: 0; overflow: auto">
                <div class="content" style="padding-top: 16px">
                    <router-view />
                </div>
            </div>
            <el-footer style="margin: auto">
                Copyright @ 2023　<a href="http://fff666.top">元扫雷网 fff666.top</a>　版权所有　<a
                    href="https://beian.miit.gov.cn/">苏ICP备2023056839号-1</a>
                <span style="width: 12px; display: inline-block"></span>
                <a href="https://beian.mps.gov.cn/#/query/webSearch?code=32020602001691" rel="noreferrer"
                    target="_blank">苏公网安备32020602001691</a>
            </el-footer>
        </el-container>
    </div>

    <el-dialog draggable :lock-scroll="false" v-model="notice_visible" title="站长通知" width="30%"
        :before-close="handle_notice_close">
        <span>{{ notice }}</span>
        <template #footer>
            <span class="dialog-footer">
                <el-checkbox v-model="never_show_notice">不再显示此对话框</el-checkbox>
                <el-button type="primary" @click="handle_notice_close()">
                    确认
                </el-button>
            </span>
        </template>
    </el-dialog>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from "vue";
import LanguagePicker from "./components/LanguagePicker.vue";
import Login from "./components/Login.vue";
// import { LoginStatus } from "@/utils/common/structInterface"
import useCurrentInstance from "@/utils/common/useCurrentInstance";
import { useLocalStore, useUserStore } from "./store";
const store = useUserStore();
const local = useLocalStore();

import { useI18n } from "vue-i18n";
const t = useI18n();

const { proxy } = useCurrentInstance();
import logo_1 from "@/assets/logo.png";
import logo_2 from "@/assets/logo2.png";

import { useRouter } from "vue-router";
const router = useRouter();

import { useDark, useToggle } from '@vueuse/core';
const isDark = useDark()
useToggle(isDark)

// const player_visible = ref(false)
const notice_visible = ref(false);
const never_show_notice = ref(false);

// 主要是切换后的高亮
const menu_index = ref();

const menu_items = [
    { index: "ranking", icon: "Trophy", content: "menu.ranking" },
    { index: "video", icon: "VideoCameraFilled", content: "menu.video" },
    { index: "world", icon: "Odometer", content: "menu.world" },
    { index: "guide", icon: "Document", content: "menu.guide" },
    { index: "score", icon: "Histogram", content: "menu.score" },
];

const notice = ref(`
1、即日起开始删档公测，公测与开发同步进行。公测结束后，在正式上线之前会删除所有数据。
2、相关意见、问题和建议请移步至此处[https://gitee.com/ee55/saolei_website/issues]发表。
`);

onMounted(() => {
    const notice_hash = localStorage.getItem("notice") as String;
    if (hash_code(notice.value) + "" != notice_hash) {
        notice_visible.value = true;
    }

    console.log(`
  元扫雷网(fff666.top)开发团队，期待您的加入: 2234208506@qq.com
  `);
    router.isReady().then(() => {
        menu_index.value = router.currentRoute.value.fullPath;
    });
});

const player_url = computed(() => {
    return "/player/" + store.user.id;
});

const user_login = () => {
    // player_visible.value = true;
    // tab_width.value = "14vw";
};

const user_logout = () => {
    // console.log(router.currentRoute.value.fullPath);
    // 如果切在我的地盘，就切到主页
    if (router.currentRoute.value.fullPath.slice(0, 7) == "/player") {
        menu_index.value = "/";
        proxy.$router.push("/");
    }
};

// const goback_home = () => {
//     router.push("/")
// }

// 站长通知关闭的回调
const handle_notice_close = () => {
    if (never_show_notice.value) {
        localStorage.setItem("notice", hash_code(notice.value) + "");
    }
    notice_visible.value = false;
};

const hash_code = function (t: string) {
    var hash = 0,
        i,
        chr;
    if (t.length === 0) return hash;
    for (i = 0; i < t.length; i++) {
        chr = t.charCodeAt(i);
        hash = (hash << 5) - hash + chr;
        hash |= 0; // 32bit integer
    }
    return hash;
};
</script>

<style lang="less">
body {
    overflow: auto;
    margin: 0;
}

</style>

<style lang="less" scoped>

.logo {
    cursor: pointer;
    display: inline-flex; 
    justify-content: center; 
    align-items: center;
    padding: 0px;
    padding-left: v-bind("local.menu_height / 8 + 'px'");
    padding-right: v-bind("local.menu_height / 8 + 'px'");
}

.logo1 {
    width: v-bind("local.menu_height - 8 + 'px'");
    height: v-bind("local.menu_height - 8 + 'px'");
    padding-top: 4px;
    padding-bottom: 4px;
    display: inline-flex;
}

.logo2 {
    width: v-bind("local.menu_height * 2.17 + 'px'");
    height: v-bind("local.menu_height + 'px'");
    display: inline-flex;
}

.header {
    font-size: 18px;
    margin: 0px;
    padding-top: 21px;
}

.menu {
    height: v-bind("local.menu_height + 'px'");
    position: fixed;
    width: 100%;
    z-index: 1010; //message的z索引为2015
    user-select: none;
    overflow-x: auto;
    overflow-y: hidden;
}

.menuicon {
    width: 60px;
    height: 60px;
}

.menuitem {
    font-size: v-bind("local.menu_font_size + 'px'");
    padding-left: 8px;
    padding-right: 5px;
}

.menumargin {
    margin-top: 0px;
    margin-bottom: 0px;
}

/*设置点击前的样式 */
a {
    text-decoration: none;
    color: #000;
}

/*设置点击后的样式 */
.router-link-active {
    text-decoration: none;
    color: #000;
}

.header_all {
    margin: auto;
    width: 80vw;
}

.content {
    margin-top: v-bind("local.menu_height + 'px'");
}

.clickable:hover {
    color: rgb(26, 127, 228);
    cursor: pointer;
}
</style>
