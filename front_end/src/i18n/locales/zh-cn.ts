import { LocaleConfig } from '@/i18n/config'

export const zhCn = {
    local: 'zh-cn',
    name: '简体中文',
    common: {
        action: {
            getSoftware: '获取录像信息',
            getUserProfile: '查询用户',
            getVideoModel: '查询录像',
            setUserProfile: '修改用户',
            setVideoModel: '修改录像',
            uploadFile: '上传文件',
            videoQuery: '查询录像',
        },
        hide: '隐藏',
        level: {
            b: '初级',
            i: '中级',
            e: '高级',
            sum: '总计',
        },
        mode: {
            std: '标准',
            nf: '盲扫',
            ng: '无猜',
            dg: '递归'
        },
        msg: {
            actionFail: '{0}失败！',
            actionSuccess: '{0}成功',
            agreeTAC: '请同意用户协议！',
            confirmPasswordFail: '两次输入的密码不一致！',
            connectionFail: '无法连接到服务器！',
            emailCodeSent: '获取验证码成功，请至邮箱查看！',
            emptyEmail: '请输入邮箱！',
            emptyEmailCode: '请输入6位邮箱验证码！',
            emptyPassword: '请输入密码！',
            emptyUsername: '请输入用户名！',
            fileTooLarge: '文件大小不能超过{0}',
            invalidEmail: '邮箱格式不正确！',
            invalidEmailCode: '邮箱验证码格式不正确！请点击邮箱验证码并打开邮箱查收。',
            invalidPassword: '密码格式不正确！长度应该为6-20位。',
            invalidUsername: '用户名格式不正确！长度不超过20位。',
            logoutFail: '退出失败！',
            logoutSuccess: '退出成功！',
            realNameRequired: '请修改为实名',
        },
        prop: {
            action: '操作',
            identifier: '标识',
            fileName: '文件名',
            is: '岛',
            level: '级别',
            op: '空',
            realName: '姓名',
            sex: '性别',
            status: '状态',
            time: '用时',
            timems: '用时',
            upload_time: '上传时间',
        },
        response: {
            OK: '',
            BadRequest: '无法识别的请求',
            Forbidden: '权限不足',
            InternalServerError: '后端发生错误',
            NotFound: '找不到数据',
            PayloadTooLarge: '文件过大',
            TooManyRequests: '请求过于频繁',
            UnsupportedMediaType: '不支持的文件类型',
        },
        show: '显示',
        software: {
            resource_download: '资源下载',
            software_download: '软件下载',
            download_link: '下载链接',
            metasweeper: '元扫雷',
            metasweeper_int: '（开源扫雷网官方扫雷软件，包含八种模式的无猜扫雷、第三代录像播放器、自带光学识别求解器。）', // introduction
            arbiter_int: '（同时受到国际网、中国扫雷网、开源扫雷网认可的老牌扫雷软件，只有标准模式。）',
        },
        toDo: '敬请期待',
    },
    footer: {
        contact: '联系我们',
        donate: '捐赠',
        team: '团队',
        links: '友链',
        about: '关于我们',
    },
    forgetPassword: {
        title: '找回密码',
        captcha: '验证码',
        confirm: '确认修改密码',
        confirmPassword: '请输入确认密码',
        email: '请输入邮箱',
        emailCode: '请输入邮箱验证码',
        getEmailCode: '获取邮箱验证码',
        password: '请输入新的6-20位密码',
        success: '修改密码成功！',
    },
    guide: {
        announcement: '公告',
        other: '其他',
        skill: '技术',
        tutorial: '教程',
    },
    home: {
        news: '新闻',
        latestScore: '最新录像',
        reviewQueue: '审核队列',
    },
    login: {
        title: '欢迎登录',
        username: '用户名',
        password: '密码',
        captcha: '验证码',
        forgetPassword: '（找回密码）',
        keepMeLoggedIn: '记住我',
        confirm: '登录'
    },
    menu: {
        ranking: '排行榜',
        video: '录像',
        world: '统计',
        guide: '教程',
        score: '积分',
        profile: '我的地盘',
        welcome: '欢迎您，{0}！',
        login: '登录',
        logout: '退出',
        register: '注册',
        setting: '设置',
    },
    news: {
        breakRecordTo: '将{mode}{level}{stat}纪录刷新为',
    },
    profile: {
        changeAvatar: '*点击图片修改头像',
        realname: '姓名：',
        realnameInput: '请输入真实姓名',
        signature: '个人简介',
        signatureInput: '请输入个人简介',
        change: '修改简介',
        confirmChange: '确认',
        cancelChange: '取消',
        identifier: '我的标识：',
        msg: {
            avatarChange: '头像修改成功！剩余{0}次',
            avatarFormat: '头像必须为JPG或PNG格式！',
            avatarFilesize: '头像大小不能超过50MB！',
            realnameChange: '姓名修改成功！剩余{0}次',
            signatureChange: '个性签名修改成功！剩余{0}次',
        },
        records: {
            title: '个人纪录',
            modeRecord: '模式纪录：'
        },
        videos: '全部录像',
        upload: {
            title: '上传录像',
            dragOrClick: `将录像拉到此处或 <em>点击此处选择</em>`,
            uploadAll: '一键上传（{0}个）',
            cancelAll: '全部清空',
            constraintNote: '*单个文件大小不能超过5MB',
            error: {
                collision: '录像已存在',
                custom: '暂不支持自定义级别',
                identifier: '标识不匹配',
                fail: '不通过',
                fileext: '无法识别的文件类型',
                filename: '文件名超过了100字节',
                filesize: '文件大小超过了5MB',
                pass: '通过',
                process: '上传中',
                upload: '上传失败',
            }
        }
    },
    register: {
        title: '用户注册',
        username: '请输入用户昵称（唯一、登录凭证、无法修改）',
        email: '请输入邮箱（唯一）',
        captcha: '验证码',
        getEmailCode: '获取邮箱验证码',
        emailCode: '请输入邮箱验证码',
        password: '请输入6-20位密码',
        confirmPassword: '请输入确认密码',
        agreeTo: '已阅读并同意',
        termsAndConditions: '开源扫雷网用户协议',
        confirm: '注册',
    },
    setting: {
        appearance: '外观设置',
        colorscheme: {
            auto: '自动',
            dark: '深色',
            light: '浅色',
            title: '颜色主题',
        },
        languageSwitch: '语言切换',
        menuFontSize: '菜单字号',
        menuHeight: '菜单高度',
        menuLayout: '菜单排版',
        menuLayoutAbstract: '抽象',
        menuLayoutDefault: '默认',
    },
    team: {
        title: '团队',
        owner: '站长',
        moderator: '管理员',
        software: '开发',
        localization: '本地化',
        zhCn: '简体中文',
        en: '英语',
        de: '德语',
        pl: '波兰语',
        designer: '外观设计',
        acknowledgement: '致谢',
    },
}
