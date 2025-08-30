使用[GitHub Action](https://github.com/features/actions)+[Selenium](https://selenium.dev)实现雀魂每日5:00自动登录，完成“良好市民”成就

![image](https://github.com/QuanQuan-CHO/Majsoul-Login/assets/90035785/9b7fac02-79cb-4e5c-b98d-7f1788d5996d)

或者自动完成某些活动任务：
<img width="1999" height="1038" alt="image" src="https://github.com/user-attachments/assets/250c1e21-7092-4265-b75e-88eb99001c0d" />


浏览器F12抓包太麻烦，所以干脆用了Selenium

[GitHub Action的Ubuntu内置了Chrome浏览器](https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2204-Readme.md#browsers-and-drivers)，无需手动安装，由于没有桌面环境，需要[使用headless模式启动Chrome](https://selenium.dev/blog/2023/headless-is-going-away)

其他参考：
- [Selenium Mouse API](https://selenium.dev/documentation/webdriver/actions_api/mouse)
- https://tecadmin.net/setup-selenium-with-python-on-ubuntu-debian
- https://zhuanlan.zhihu.com/p/632399597
<br>

## 使用方法
1. Fork本仓库
2. 点击Settings->Secrets and variables->Actions->New repository secret，依次配置`EMAIL`、`PASSWD`
    - EMAIL 是雀魂的邮箱账号，如有多个账户用空格分隔，例如`example@gmail.com example@qq.com`
    - PASSWD 是雀魂的密码，如有多个账户用空格分隔，与邮箱依次对应，例如`grc28r7g3 pdtaw3fwag`
3. 先在Actions页面将GitHub Action启用，再选择对应的workflow，将scheduled workflow启用
   ![enable-schedule-workflow](https://user-images.githubusercontent.com/90035785/224888848-be15ba52-1892-4a2b-9cef-b321b9a25165.jpg)
4. Enjoy it!
