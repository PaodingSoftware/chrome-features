# Chrome Switches Review

Generated on: 2025-07-22 16:06:48
Total switches: 1444

## 说明
- [ ] 审核每个开关后勾选复选框
- [ ] 根据需要在"审核备注"列中添加注释
- [ ] 使用#重要、#已弃用、#实验性等标签进行分类

## Accessibility (11 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0001"> | `disable-renderer-accessibility` | `kDisableRendererAccessibility` | 在渲染器中关闭辅助功能。 |  |
| <input type="checkbox" unchecked id="switch_0002"> | `enable-experimental-accessibility-autoclick` | `kEnableExperimentalAccessibilityAutoclick` | 显示尚未发布的额外自动点击功能。 |  |
| <input type="checkbox" unchecked id="switch_0003"> | `enable-experimental-accessibility-labels-debugging` | `kEnableExperimentalAccessibilityLabelsDebugging` | 启用对辅助功能标签特性的可视化调试支持，该特性为屏幕阅读器用户提供图像描述。 |  |
| <input type="checkbox" unchecked id="switch_0004"> | `enable-experimental-accessibility-language-detection` | `kEnableExperimentalAccessibilityLanguageDetection` | 在页面文本内容上启用语言检测，然后将其暴露给屏幕阅读器等辅助技术。 |  |
| <input type="checkbox" unchecked id="switch_0005"> | `enable-experimental-accessibility-language-detection-dynamic` | `kEnableExperimentalAccessibilityLanguageDetectionDynamic` | 为动态内容启用语言检测，然后将其暴露给屏幕阅读器等辅助技术。 |  |
| <input type="checkbox" unchecked id="switch_0006"> | `enable-experimental-accessibility-manifest-v3` | `kEnableExperimentalAccessibilityManifestV3` | 在迁移仍在进行中时，将辅助功能扩展切换为使用扩展清单v3。 |  |
| <input type="checkbox" unchecked id="switch_0007"> | `enable-experimental-accessibility-switch-access-text` | `kEnableExperimentalAccessibilitySwitchAccessText` | 为文本输入启用正在开发中的开关访问功能。 |  |
| <input type="checkbox" unchecked id="switch_0008"> | `enable-mac-accessibility-api-migration` | `kEnableMacAccessibilityAPIMigration` | 启用切换到较新的基于NSAccessibility属性的API。 |  |
| <input type="checkbox" unchecked id="switch_0009"> | `enable-magnifier-debug-draw-rect` | `kEnableMagnifierDebugDrawRect` | 启用在放大区域周围绘制矩形的调试功能，无需放大。 |  |
| <input type="checkbox" unchecked id="switch_0010"> | `force-renderer-accessibility` | `kForceRendererAccessibility` | 强制启用渲染器辅助功能，而不是在检测到屏幕阅读器时按需启用。如果存在disable-renderer-accessibility开关，则会覆盖此开关。此开关有一个可选参数，可强制AXMode捆绑。三个可用的捆绑设置是：'basic'、'form-controls'和'complete'。如果捆绑参数无效，则强制AXMode将默认为'complete'。如果缺少捆绑参数，则初始AXMode将默认为complete，但允许在执行期间更改AXMode。 |  |
| <input type="checkbox" unchecked id="switch_0011"> | `generate-accessibility-test-expectations` | `kGenerateAccessibilityTestExpectations` |  |  |

## Android Webview Aw Switches.cc (26 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0012"> | `debug-bsa` | `kDebugBsa` | 覆盖并启用对BSA库测试/调试有用的功能。 |  |
| <input type="checkbox" unchecked id="switch_0013"> | `finch-seed-expiration-age` | `kFinchSeedExpirationAge` | 应用程序的变体种子副本被视为新鲜的时间长度（以秒为单位）。如果应用程序的种子比这个时间更旧，将从WebView的IVariationsSeedServer请求新的种子。 |  |
| <input type="checkbox" unchecked id="switch_0014"> | `finch-seed-ignore-pending-download` | `kFinchSeedIgnorePendingDownload` | 强制WebView的服务始终调度新的变体种子下载作业，即使已有一个作业正在等待。 |  |
| <input type="checkbox" unchecked id="switch_0015"> | `finch-seed-min-download-period` | `kFinchSeedMinDownloadPeriod` | WebView服务在两次从变体服务器下载变体种子之间等待的最小时间（以秒为单位）。 |  |
| <input type="checkbox" unchecked id="switch_0016"> | `finch-seed-min-update-period` | `kFinchSeedMinUpdatePeriod` | 嵌入式WebView实现在两次向WebView服务请求新变体种子之间等待的最小时间（以秒为单位）。 |  |
| <input type="checkbox" unchecked id="switch_0017"> | `finch-seed-no-charging-requirement` | `kFinchSeedNoChargingRequirement` | 强制WebView的服务始终调度新的变体种子下载作业，即使设备未在充电。请注意，此开关对于在Android模拟器上进行测试可能是必要的，因为这些模拟器并不总是被认为在充电。 |  |
| <input type="checkbox" unchecked id="switch_0018"> | `highlight-all-webviews` | `kHighlightAllWebViews` | 用黄色色调突出显示所有WebView的内容（包括Web内容）。这对于在Android应用程序中识别WebView很有用。 |  |
| <input type="checkbox" unchecked id="switch_0019"> | `net-log` | `kNetLog` | 从WebView启用网络日志记录。这捕获网络活动以进行调试，并将文件存储在DevUi中。 |  |
| <input type="checkbox" unchecked id="switch_0020"> | `webview-disable-safebrowsing-support` | `kWebViewDisableSafebrowsingSupport` | 用于在webview中禁用安全浏览功能 |  |
| <input type="checkbox" unchecked id="switch_0021"> | `webview-enable-modern-cookie-same-site` | `kWebViewEnableModernCookieSameSite` | 启用现代SameSite cookie行为（与传统行为相对）。这用于在现代行为默认启用之前的WebView版本。这启用了same-site-by-default-cookies、cookies-without-SameSite-must-be-secure和schemeful-same-site功能。 |  |
| <input type="checkbox" unchecked id="switch_0022"> | `webview-fenced-frames` | `kWebViewFencedFrames` | 启用FencedFrames。这也启用了PrivacySandboxAdsAPIsOverride。 |  |
| <input type="checkbox" unchecked id="switch_0023"> | `webview-force-crash-java` | `kWebViewForceCrashJava` | 在Java层的WebView启动期间启用崩溃 |  |
| <input type="checkbox" unchecked id="switch_0024"> | `webview-force-crash-native` | `kWebViewForceCrashNative` | 在原生层的WebView启动期间启用崩溃 |  |
| <input type="checkbox" unchecked id="switch_0025"> | `webview-force-disable-3pcs` | `kWebViewForceDisable3pcs` | 强制为所有应用禁用第三方cookie。 |  |
| <input type="checkbox" unchecked id="switch_0026"> | `webview-fps-component` | `kWebViewFpsComponent` | 在非嵌入式WebView中通过组件更新器下载服务启用FirstPartySetsComponentInstallerPolicy的下载。 |  |
| <input type="checkbox" unchecked id="switch_0027"> | `webview-log-js-console-messages` | `kWebViewLogJsConsoleMessages` |  |  |
| <input type="checkbox" unchecked id="switch_0028"> | `webview-masked-domain-list-component` | `kWebViewMaskedDomainListComponent` | 在非嵌入式WebView中通过组件更新器下载服务启用MaskedDomainListComponentInstallerPolicy的下载。 |  |
| <input type="checkbox" unchecked id="switch_0029"> | `webview-safebrowsing-block-all-resources` | `kWebViewSafebrowsingBlockAllResources` | 启用SafeBrowsing并使WebView将所有资源视为恶意。小心使用：这将阻止所有资源加载。 |  |
| <input type="checkbox" unchecked id="switch_0030"> | `webview-sandboxed-renderer` | `kWebViewSandboxedRenderer` |  |  |
| <input type="checkbox" unchecked id="switch_0031"> | `webview-selective-image-inversion-darkening` | `kWebViewSelectiveImageInversionDarkening` | 启用使用选择性图像反转来自动暗化页面，当WebView处于暗模式但网站没有提供暗样式时使用。 |  |
| <input type="checkbox" unchecked id="switch_0032"> | `webview-startup-tasks-yield-to-native` | `kWebViewStartupTasksYieldToNative` | 如果WebView启动是异步的，则启用异步运行原生启动任务。 |  |
| <input type="checkbox" unchecked id="switch_0033"> | `webview-tpcd-metadata-component` | `kWebViewTpcdMetadaComponent` | 在非嵌入式WebView中通过组件更新器下载服务启用TpcdMetadataComponentInstallerPolicy的下载。 |  |
| <input type="checkbox" unchecked id="switch_0034"> | `webview-use-separate-resource-context` | `kWebViewUseSeparateResourceContext` | 使用WebView的上下文进行资源查找，而不是嵌入应用程序的上下文。 |  |
| <input type="checkbox" unchecked id="switch_0035"> | `webview-use-startup-tasks-logic` | `kWebViewUseStartupTasksLogic` | 启用使用启动任务逻辑进行webview chromium初始化，该逻辑：如果启动是从后台线程触发的，则异步运行启动任务。否则同步运行启动。缓存任何chromium启动异常，如果在没有重新启动的情况下重试启动，则重新抛出。 |  |
| <input type="checkbox" unchecked id="switch_0036"> | `webview-use-startup-tasks-logic-p2` | `kWebViewUseStartupTasksLogicP2` | 启用webview chromium初始化使用启动任务逻辑的第二阶段，该阶段在异步启动webview时也异步启动浏览器进程。 |  |
| <input type="checkbox" unchecked id="switch_0037"> | `webview-verbose-logging` | `kWebViewVerboseLogging` | WebView将向logcat记录额外的调试信息，例如变体和命令行状态。 |  |

## Ash Constants Ash Switches.cc (251 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0038"> | `aggressive-cache-discard` | `kAggressiveCacheDiscardThreshold` |  |  |
| <input type="checkbox" unchecked id="switch_0039"> | `allow-empty-passwords-in-tests` | `kTemporaryAllowEmptyPasswordsInTests` | TODO(b/299642185): 在2023年底前删除此标志。ChromeOS不支持用户使用空密码，但一些旧的测试设置可能对用户使用空密码。 |  |
| <input type="checkbox" unchecked id="switch_0040"> | `allow-failed-policy-fetch-for-test` | `kAllowFailedPolicyFetchForTest` | 如果传递了此标志，失败的策略获取将不会导致配置文件初始化失败。这对测试很有用，因为这意味着测试不必模拟策略基础设施。 |  |
| <input type="checkbox" unchecked id="switch_0041"> | `allow-os-install` | `kAllowOsInstall` | 当设置此标志时，可以访问OS安装UI。这允许用户从USB安装到磁盘。 |  |
| <input type="checkbox" unchecked id="switch_0042"> | `almanac-api-url` | `kAlmanacApiUrl` | 覆盖用于ChromeOS Almanac API的URL。用于使用非生产服务器进行本地测试（例如"--almanac-api-url=http://localhost:8000"）。 |  |
| <input type="checkbox" unchecked id="switch_0043"> | `always-enable-hdcp` | `kAlwaysEnableHdcp` | 当连接外部显示器时，使指定类型的HDCP始终启用。用于ChromeOS上的HDCP合规测试。 |  |
| <input type="checkbox" unchecked id="switch_0044"> | `app-auto-launched` | `kAppAutoLaunched` | 指定在信息亭模式下启动的应用是否以零延迟自动启动。用于在会话恢复流程中正确恢复自动启动状态。 |  |
| <input type="checkbox" unchecked id="switch_0045"> | `app-mode-oem-manifest` | `kAppOemManifestFile` | 应用OEM清单文件的路径。 |  |
| <input type="checkbox" unchecked id="switch_0046"> | `arc-availability` | `kArcAvailability` | 在此设备上发出ARC支持状态信号。这可以取以下三个值之一：- none：此设备上未安装ARC。（默认）- installed：此设备上安装了ARC，但未正式支持。只有在Finch实验开启时，用户才能启用ARC。- officially-supported：此设备上安装并支持ARC。因此用户可以通过设置等启用ARC。 |  |
| <input type="checkbox" unchecked id="switch_0047"> | `arc-available` | `kArcAvailable` | 已弃用：请使用--arc-availability=installed。在此设备上发出ARC实例可用性信号。 |  |
| <input type="checkbox" unchecked id="switch_0048"> | `arc-block-keymint` | `kArcBlockKeyMint` | 阻止KeyMint的开关。当KeyMint被阻止时，Keymaster将被启用。 |  |
| <input type="checkbox" unchecked id="switch_0049"> | `arc-data-cleanup-on-start` | `kArcDataCleanupOnStart` | 强制在每次启动时清理ARC数据的标志。 |  |
| <input type="checkbox" unchecked id="switch_0050"> | `arc-disable-app-sync` | `kArcDisableAppSync` | 禁用静默安装某些应用的ARC应用同步流程的标志。在自动测试中用于解决竞态条件。 |  |
| <input type="checkbox" unchecked id="switch_0051"> | `arc-disable-dexopt-cache` | `kArcDisableDexOptCache` | 在测试中用于禁用默认开启的DexOpt缓存。 |  |
| <input type="checkbox" unchecked id="switch_0052"> | `arc-disable-download-provider` | `kArcDisableDownloadProvider` | 禁用ARC下载提供程序的标志，该程序阻止在Play Store和GMS Core上下文中下载和安装额外内容。 |  |
| <input type="checkbox" unchecked id="switch_0053"> | `arc-disable-gms-core-cache` | `kArcDisableGmsCoreCache` | 在自动测试中用于禁用默认开启的GMS核心缓存。 |  |
| <input type="checkbox" unchecked id="switch_0054"> | `arc-disable-locale-sync` | `kArcDisableLocaleSync` | 禁用与Android容器的ARC语言环境同步的标志。在自动测试中用于防止某些应用（包括Play Store）可能重新启动的情况。重新启动Play Store可能导致随机测试失败。启用此标志还会强制ARC容器使用'en-US'作为语言环境，使用'en-US,en'作为首选语言。 |  |
| <input type="checkbox" unchecked id="switch_0055"> | `arc-disable-media-store-maintenance` | `kArcDisableMediaStoreMaintenance` | 用于禁用GMS调度的媒体存储定期索引和语料库维护任务。在性能测试中使用，以防止在测试期间运行，这可能导致不稳定的结果或CPU在测试前非空闲失败。 |  |
| <input type="checkbox" unchecked id="switch_0056"> | `arc-disable-play-auto-install` | `kArcDisablePlayAutoInstall` | 禁用静默安装预定义应用集的ARC Play自动安装流程的标志。在自动测试中用于解决竞态条件。 |  |
| <input type="checkbox" unchecked id="switch_0057"> | `arc-disable-tts-cache` | `kArcDisableTtsCache` | 在自动测试中用于禁用默认开启的TTS缓存。 |  |
| <input type="checkbox" unchecked id="switch_0058"> | `arc-enable-attestation` | `kArcEnableAttestation` | 为KeyMint启用密钥和ID证明的标志。 |  |
| <input type="checkbox" unchecked id="switch_0059"> | `arc-erofs` | `kArcErofs` | 指示ARC镜像使用EROFS格式的标志（go/arcvm-erofs）。 |  |
| <input type="checkbox" unchecked id="switch_0060"> | `arc-force-mount-android-volumes-in-files` | `kArcForceMountAndroidVolumesInFiles` | 强制在Files应用中挂载Android卷（DocumentsProviders和Play文件）的标志。用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0061"> | `arc-force-show-optin-ui` | `kArcForceShowOptInUi` | 强制显示OptIn UI的标志。用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0062"> | `arc-generate-play-auto-install` | `kArcGeneratePlayAutoInstall` | 启用生成ARC Play自动安装名单所需的开发者选项的标志。由开发者手动使用。 |  |
| <input type="checkbox" unchecked id="switch_0063"> | `arc-host-ureadahead-mode` | `kArcHostUreadaheadMode` | 设置ARC容器启动期间ureadahead的操作模式。readahead（默认）- 在生产中使用，等同于未设置开关。generate - 在Android Uprev数据收集器期间使用，预生成包文件并上传到Google Cloud作为CrOS构建镜像的构建工件。disabled - 用于测试目的，在ARC容器启动期间禁用ureadahead。 |  |
| <input type="checkbox" unchecked id="switch_0064"> | `arc-install-event-chrome-log-for-tests` | `kArcInstallEventChromeLogForTests` | 将ARC++安装事件写入chrome日志用于集成测试。 |  |
| <input type="checkbox" unchecked id="switch_0065"> | `arc-packages-cache-mode` | `kArcPackagesCacheMode` | 在自动测试中用于指定如何处理包缓存。可以是：copy - 将生成的packages.xml复制到临时目录。skip-copy - 跳过初始包缓存设置并将生成的packages.xml复制到临时目录。 |  |
| <input type="checkbox" unchecked id="switch_0066"> | `arc-play-store-auto-update` | `kArcPlayStoreAutoUpdate` | 在自动测试中用于强制Play Store自动更新状态。可以是：on - 强制开启自动更新。off - 强制关闭自动更新。 |  |
| <input type="checkbox" unchecked id="switch_0067"> | `arc-scale` | `kArcScale` | 为ARC应用设置缩放比例。这是以DPI为单位。例如280 DPI约为1.75设备缩放因子。参见https://source.android.com/compatibility/android-cdd#3_7_runtime_compatibility获取支持的DPI值列表。 |  |
| <input type="checkbox" unchecked id="switch_0068"> | `arc-start-mode` | `kArcStartMode` | 定义如何启动ARC。这可以取以下值之一：- always-start 自动启动并支持Play Store UI。- always-start-with-no-play-store 自动启动但不支持Play Store UI。如果未设置，则ARC以默认模式启动。 |  |
| <input type="checkbox" unchecked id="switch_0069"> | `arc-tos-host-for-tests` | `kArcTosHostForTests` | 为测试设置ARC服务条款主机名url。 |  |
| <input type="checkbox" unchecked id="switch_0070"> | `arc-use-dev-caches` | `kArcUseDevCaches` | 指示ARC使用由Uprev中数据收集器生成的开发缓存，而不是来自CrOS构建阶段的缓存用于arccachesetup服务的标志。 |  |
| <input type="checkbox" unchecked id="switch_0071"> | `arcvm-ureadahead-mode` | `kArcVmUreadaheadMode` | 设置ARCVM启动期间ureadahead的操作模式。如果未设置此开关，ARCVM ureadahead将检查包文件的存在和年龄，并预读文件到页面缓存以改善启动性能。readahead（默认）- 在生产中使用，等同于未设置开关。这在tast测试中用于显式开启guest ureadahead（参见\|kArcDisableUreadahead\|）。generate - 在Android Uprev数据收集器期间使用，预生成包文件并上传到Google Cloud作为CrOS构建镜像的构建工件。disabled - 用于测试目的，在ARCVM启动期间禁用ureadahead。注意，\|kArcDisableUreadahead\|也会禁用guest和host两部分的ureadahead。 |  |
| <input type="checkbox" unchecked id="switch_0072"> | `arcvm-use-hugepages` | `kArcVmUseHugePages` | 建议内核对guest内存使用大页面。 |  |
| <input type="checkbox" unchecked id="switch_0073"> | `ash-allow-default-shelf-pin-layout-ignoring-sync` | `kAllowDefaultShelfPinLayoutIgnoringSync` | 允许Ash货架应用默认固定布局，而无需等待Sync从服务器下载数据（许多测试无法实现）。 |  |
| <input type="checkbox" unchecked id="switch_0074"> | `ash-clear-fast-ink-buffer` | `kAshClearFastInkBuffer` | 在创建时清除快速墨水缓冲区。这在某些不清零新缓冲区的设备上是必需的。 |  |
| <input type="checkbox" unchecked id="switch_0075"> | `ash-constrain-pointer-to-root` | `kAshConstrainPointerToRoot` | 强制指针（光标）位置保持在根窗口内。 |  |
| <input type="checkbox" unchecked id="switch_0076"> | `ash-contextual-nudges-interval` | `kAshContextualNudgesInterval` | 覆盖显示用户上下文提示之间必须经过的最短时间。时间单位为秒。 |  |
| <input type="checkbox" unchecked id="switch_0077"> | `ash-contextual-nudges-reset-shown-count` | `kAshContextualNudgesResetShownCount` | 在登录时重置上下文提示显示计数。 |  |
| <input type="checkbox" unchecked id="switch_0078"> | `ash-debug-shortcuts` | `kAshDebugShortcuts` | 启用对调试有用的键盘快捷键。 |  |
| <input type="checkbox" unchecked id="switch_0079"> | `ash-dev-shortcuts` | `kAshDeveloperShortcuts` | 启用仅供开发者使用的键盘快捷键。 |  |
| <input type="checkbox" unchecked id="switch_0080"> | `ash-disable-touch-exploration-mode` | `kAshDisableTouchExplorationMode` | 禁用触摸探索模式。设置此标志时，当启用语音反馈时将不再自动开启触摸探索模式。 |  |
| <input type="checkbox" unchecked id="switch_0081"> | `ash-enable-magnifier-key-scroller` | `kAshEnableMagnifierKeyScroller` | 启用键绑定来滚动放大的屏幕。 |  |
| <input type="checkbox" unchecked id="switch_0082"> | `ash-enable-palette-on-all-displays` | `kAshEnablePaletteOnAllDisplays` | 在每个显示器上启用调色板，而不仅仅是内部显示器。 |  |
| <input type="checkbox" unchecked id="switch_0083"> | `ash-hide-notifications-for-factory` | `kAshHideNotificationsForFactory` | 隐藏与Chrome OS设备工厂测试无关的通知，如电池电量更新。 |  |
| <input type="checkbox" unchecked id="switch_0084"> | `ash-no-nudges` | `kAshNoNudges` | 隐藏可能干扰tast集成测试的教育提示。在某种程度上类似于--no-first-run，但影响系统UI行为，而不是浏览器行为。 |  |
| <input type="checkbox" unchecked id="switch_0085"> | `ash-power-button-position` | `kAshPowerButtonPosition` | 电源按钮位置包括电源按钮的物理显示侧面和电源按钮中心位置相对于landscape_primary屏幕方向下显示器宽度/高度的百分比。值是包含"position"属性的JSON对象，值为"left"、"right"、"top"或"bottom"。对于"left"和"right"，"y"属性指定按钮的中心位置作为显示器高度的分数（在[0.0, 1.0]中），相对于显示器顶部。对于"top"和"bottom"，"x"属性给出位置作为显示器宽度的分数，相对于显示器左侧。 |  |
| <input type="checkbox" unchecked id="switch_0086"> | `ash-side-volume-button-position` | `kAshSideVolumeButtonPosition` | 在landscape primary屏幕方向下侧音量按钮的物理位置信息。值是包含"region"属性（值为"keyboard"、"screen"）和"side"属性（值为"left"、"right"、"top"、"bottom"）的JSON对象。 |  |
| <input type="checkbox" unchecked id="switch_0087"> | `ash-touch-hud` | `kAshTouchHud` | 启用用于跟踪触摸点的平视显示器。 |  |
| <input type="checkbox" unchecked id="switch_0088"> | `aue-reached-for-update-required-test` | `kUpdateRequiredAueForTest` | 如果传递此开关，设备策略DeviceMinimumVersion假设设备已达到自动更新到期。这对在DUT上测试策略行为很有用。 |  |
| <input type="checkbox" unchecked id="switch_0089"> | `aura-legacy-power-button` | `kAuraLegacyPowerButton` | （大多数）Chrome OS硬件正确报告ACPI电源按钮释放。标准硬件在按下后立即报告释放。如果设置，我们会立即响应按下而锁定屏幕或关闭系统，而不是显示交互式动画。 |  |
| <input type="checkbox" unchecked id="switch_0090"> | `birch-is-evening` | `kBirchIsEvening` | 设置birch排名器假设现在是晚上，用于birch芯片排名目的。 |  |
| <input type="checkbox" unchecked id="switch_0091"> | `birch-is-morning` | `kBirchIsMorning` | 设置birch排名器假设现在是早上，用于birch芯片排名目的。 |  |
| <input type="checkbox" unchecked id="switch_0092"> | `browser-data-backward-migration-for-user` | `kBrowserDataBackwardMigrationForUser` | 指定应该为哪个用户进行浏览器数据向后迁移。 |  |
| <input type="checkbox" unchecked id="switch_0093"> | `browser-data-backward-migration-mode` | `kBrowserDataBackwardMigrationMode` | 向后迁移模式。与kBrowserDataBackwardMigrationForUser一起传递。 |  |
| <input type="checkbox" unchecked id="switch_0094"> | `browser-data-migration-for-user` | `kBrowserDataMigrationForUser` | 指定应该为哪个用户进行浏览器数据迁移。 |  |
| <input type="checkbox" unchecked id="switch_0095"> | `browser-data-migration-mode` | `kBrowserDataMigrationMode` | 运行移动迁移而不是复制。与kBrowserDataMigrationForUser一起传递。 |  |
| <input type="checkbox" unchecked id="switch_0096"> | `bwsi` | `kGuestSession` | 指示浏览器处于"无需登录浏览"（访客会话）模式。应该完全禁用扩展、同步和书签。 |  |
| <input type="checkbox" unchecked id="switch_0097"> | `campbell-key` | `kCampbellKey` | 用于传递Campbell功能密钥的开关。除非提供正确的密钥，否则无论相关功能标志的状态如何，Campbell功能都将保持禁用状态。 |  |
| <input type="checkbox" unchecked id="switch_0098"> | `cellular-first` | `kCellularFirst` | 如果设置此标志，表示此设备是"蜂窝优先"设备。蜂窝优先设备使用蜂窝电话数据网络作为连接互联网的主要方式。设置此标志有两个后果：1. 默认启用蜂窝数据漫游。2. 指示UpdateEngine允许通过蜂窝数据连接进行自动更新。 |  |
| <input type="checkbox" unchecked id="switch_0099"> | `child-wallpaper-large` | `kChildWallpaperLarge` | 用于儿童账户的默认大壁纸（作为受信任的、非用户可写的JPEG文件路径）。 |  |
| <input type="checkbox" unchecked id="switch_0100"> | `child-wallpaper-small` | `kChildWallpaperSmall` | 用于儿童账户的默认小壁纸（作为受信任的、非用户可写的JPEG文件路径）。 |  |
| <input type="checkbox" unchecked id="switch_0101"> | `clamshell` | `kAshUiModeClamshell` | kAshUiMode标志的值。 |  |
| <input type="checkbox" unchecked id="switch_0102"> | `conservative` | `kSchedulerConfigurationConservative` |  |  |
| <input type="checkbox" unchecked id="switch_0103"> | `cros-region` | `kCrosRegion` | 强制设置CrOS区域值。 |  |
| <input type="checkbox" unchecked id="switch_0104"> | `cryptohome-ignore-cleanup-ownership-for-testing` | `kCryptohomeIgnoreCleanupOwnershipForTesting` | 通常没有任何认证因子的cryptohome被认为是损坏的。特殊机制会在用户创建期间检测这种情况并删除此类用户。如果此类用户是所有者，则应该触发电源清洗。但是，如果此类事件在测试中发生，所有日志都会丢失，很难调查所有者用户配置错误的确切原因。此标志防止在此类情况下触发电源清洗，而是触发简单的用户删除。 |  |
| <input type="checkbox" unchecked id="switch_0105"> | `cryptohome-recovery-service-base-url` | `kCryptohomeRecoveryServiceBaseUrl` | 覆盖Cryptohome恢复服务的基础url。 |  |
| <input type="checkbox" unchecked id="switch_0106"> | `cryptohome-recovery-use-test-env` | `kCryptohomeRecoveryUseTestEnvironment` | 强制cryptohome恢复过程使用测试环境（测试密钥/URL）。 |  |
| <input type="checkbox" unchecked id="switch_0107"> | `cryptohome-use-authsession` | `kCryptohomeUseAuthSession` | 控制与cryptohomed交互时是否应使用AuthSession API。 |  |
| <input type="checkbox" unchecked id="switch_0108"> | `cryptohome-use-old-encryption-for-testing` | `kCryptohomeUseOldEncryptionForTesting` | 强制cryptohome使用旧的（ecryptfs）加密创建新用户。此开关可用于设置可用于测试加密迁移场景的配置。 |  |
| <input type="checkbox" unchecked id="switch_0109"> | `default-wallpaper-is-oem` | `kDefaultWallpaperIsOem` | 指示由kAshDefaultWallpaper{Large,Small}指定的壁纸图像是OEM特定的（即它们无法从Google下载）。 |  |
| <input type="checkbox" unchecked id="switch_0110"> | `default-wallpaper-large` | `kDefaultWallpaperLarge` | 要使用的默认大壁纸（作为受信任的、非用户可写的JPEG文件路径）。 |  |
| <input type="checkbox" unchecked id="switch_0111"> | `default-wallpaper-small` | `kDefaultWallpaperSmall` | 要使用的默认小壁纸（作为受信任的、非用户可写的JPEG文件路径）。 |  |
| <input type="checkbox" unchecked id="switch_0112"> | `defer-external-display-timeout` | `kDeferExternalDisplayTimeout` | 在合盖解锁或登录时等待显示器重新连接的间隔时间（秒）。 |  |
| <input type="checkbox" unchecked id="switch_0113"> | `demo-mode-enrolling-username` | `kDemoModeEnrollingUsername` | 用于演示模式的测试组织单元（OU）用户。只传递"@cros-demo-mode.com"之前的部分。 |  |
| <input type="checkbox" unchecked id="switch_0114"> | `demo-mode-force-arc-offline-provision` | `kDemoModeForceArcOfflineProvision` | 强制ARC配置采用离线演示模式的代码路径。 |  |
| <input type="checkbox" unchecked id="switch_0115"> | `demo-mode-highlights-extension` | `kDemoModeHighlightsApp` | 在演示模式下用于亮点应用的应用ID。 |  |
| <input type="checkbox" unchecked id="switch_0116"> | `demo-mode-resource-directory` | `kDemoModeResourceDirectory` | 用于获取演示模式资源内容的目录（而不是从Omaha下载）。 |  |
| <input type="checkbox" unchecked id="switch_0117"> | `demo-mode-screensaver-extension` | `kDemoModeScreensaverApp` | 在演示模式下用于屏保应用的应用ID。 |  |
| <input type="checkbox" unchecked id="switch_0118"> | `demo-mode-server-api-key` | `kDemoModeServerAPIKey` | 演示模式服务器的API密钥。 |  |
| <input type="checkbox" unchecked id="switch_0119"> | `demo-mode-server-url` | `kDemoModeServerUrl` | 覆盖生产演示模式api url用于演示账户登录。 |  |
| <input type="checkbox" unchecked id="switch_0120"> | `demo-mode-swa-content-directory` | `kDemoModeSwaContentDirectory` | 用于获取演示模式SWA内容的目录（而不是从Omaha下载）。 |  |
| <input type="checkbox" unchecked id="switch_0121"> | `derelict-detection-timeout` | `kDerelictDetectionTimeout` | OOBE中的机器被视为废弃前的时间（秒）。 |  |
| <input type="checkbox" unchecked id="switch_0122"> | `derelict-idle-timeout` | `kDerelictIdleTimeout` | 废弃机器开始演示模式前的时间（秒）。 |  |
| <input type="checkbox" unchecked id="switch_0123"> | `dev` | `kPrintingPpdChannelDev` |  |  |
| <input type="checkbox" unchecked id="switch_0124"> | `disable-arc-cpu-restriction` | `kDisableArcCpuRestriction` | 防止在ARC[VM]上设置任何CPU限制。仅供测试使用，因为如果ARC容器被节流，某些测试可能会超时。 |  |
| <input type="checkbox" unchecked id="switch_0125"> | `disable-arc-opt-in-verification` | `kDisableArcOptInVerification` | 禁用ARC选择加入验证过程，ARC默认启用。 |  |
| <input type="checkbox" unchecked id="switch_0126"> | `disable-birch-weather-api-for-testing` | `kDisableBirchWeatherApiForTesting` | 禁用Birch调用天气API。允许tast测试中的虚假用户避免使用无效的GAIA ID进行API调用，这会在天气服务器端引起错误。 |  |
| <input type="checkbox" unchecked id="switch_0127"> | `disable-demo-mode` | `kDisableDemoMode` | 禁用Chrome OS演示。 |  |
| <input type="checkbox" unchecked id="switch_0128"> | `disable-device-disabling` | `kDisableDeviceDisabling` | 如果设置此开关，设备不能被其所有者远程禁用。 |  |
| <input type="checkbox" unchecked id="switch_0129"> | `disable-drive-fs-for-testing` | `kDisableDriveFsForTesting` | 为测试目的禁用DriveFS，用于tast测试且仅在测试镜像上使用。 |  |
| <input type="checkbox" unchecked id="switch_0130"> | `disable-fine-grained-time-zone-detection` | `kDisableFineGrainedTimeZoneDetection` | 禁用细粒度时区检测。 |  |
| <input type="checkbox" unchecked id="switch_0131"> | `disable-first-run-ui` | `kDisableFirstRunUI` | 禁用显示首次运行UI。 |  |
| <input type="checkbox" unchecked id="switch_0132"> | `disable-gaia-services` | `kDisableGaiaServices` | 禁用GAIA服务，如注册和OAuth会话恢复。由'虚假'遥测登录使用。 |  |
| <input type="checkbox" unchecked id="switch_0133"> | `disable-hid-detection-on-oobe` | `kDisableHIDDetectionOnOOBEForTesting` | 禁用HID检测OOBE屏幕。 |  |
| <input type="checkbox" unchecked id="switch_0134"> | `disable-login-animations` | `kDisableLoginAnimations` | 避免在登录时执行昂贵的动画。 |  |
| <input type="checkbox" unchecked id="switch_0135"> | `disable-machine-cert-request` | `kDisableMachineCertRequest` | 在证明期间禁用企业机器证书请求。 |  |
| <input type="checkbox" unchecked id="switch_0136"> | `disable-oobe-chromevox-hint-timer-for-testing` | `kDisableOOBEChromeVoxHintTimerForTesting` | 禁用OOBE中的ChromeVox提示空闲检测，这可能在测试期间导致意外行为。 |  |
| <input type="checkbox" unchecked id="switch_0137"> | `disable-oobe-network-screen-skipping-for-testing` | `kDisableOOBENetworkScreenSkippingForTesting` | 禁用基于以太网连接的网络屏幕跳过检查。 |  |
| <input type="checkbox" unchecked id="switch_0138"> | `disable-per-user-timezone` | `kDisablePerUserTimezone` | 禁用每用户时区。 |  |
| <input type="checkbox" unchecked id="switch_0139"> | `disable-rollback-option` | `kDisableRollbackOption` | 在重置屏幕上禁用回滚选项。 |  |
| <input type="checkbox" unchecked id="switch_0140"> | `disable-volume-adjust-sound` | `kDisableVolumeAdjustSound` | 禁用音量调整声音。 |  |
| <input type="checkbox" unchecked id="switch_0141"> | `disallow-policy-block-dev-mode` | `kDisallowPolicyBlockDevMode` | 禁止通过企业设备策略阻止开发者模式：- 如果注册会阻止开发者模式，则企业注册失败。- 如果新设备策略会阻止开发者模式，则不应用。这只能在测试构建上使用。 |  |
| <input type="checkbox" unchecked id="switch_0142"> | `enable-arc` | `kEnableArc` | 已弃用。请使用--arc-availability=officially-supported。启用在会话开始时启动ARC实例。 |  |
| <input type="checkbox" unchecked id="switch_0143"> | `enable-arcvm` | `kEnableArcVm` | 启用ARCVM。 |  |
| <input type="checkbox" unchecked id="switch_0144"> | `enable-arcvm-dlc` | `kEnableArcVmDlc` | 启用ARCVM DLC。 |  |
| <input type="checkbox" unchecked id="switch_0145"> | `enable-arcvm-rt-vcpu` | `kEnableArcVmRtVcpu` | 启用ARCVM实时VCPU功能。 |  |
| <input type="checkbox" unchecked id="switch_0146"> | `enable-birch-weather-api-for-testing-override` | `kEnableBirchWeatherApiForTestingOverride` | 用于为特定tast测试覆盖kDisableBirchWeatherApiForTesting。 |  |
| <input type="checkbox" unchecked id="switch_0147"> | `enable-cast-receiver` | `kEnableCastReceiver` | 启用Cast接收器。 |  |
| <input type="checkbox" unchecked id="switch_0148"> | `enable-dim-shelf` | `kEnableDimShelf` | 为ChromeOS启用货架调暗功能。 |  |
| <input type="checkbox" unchecked id="switch_0149"> | `enable-extension-assets-sharing` | `kEnableExtensionAssetsSharing` | 启用已安装默认应用的资源共享。 |  |
| <input type="checkbox" unchecked id="switch_0150"> | `enable-houdini` | `kEnableHoudini` | 启用使用32位Houdini库进行ARM二进制转换。 |  |
| <input type="checkbox" unchecked id="switch_0151"> | `enable-houdini64` | `kEnableHoudini64` | 启用使用64位Houdini库进行ARM二进制转换。 |  |
| <input type="checkbox" unchecked id="switch_0152"> | `enable-natural-scroll-default` | `kNaturalScrollDefault` | 默认启用自然滚动。 |  |
| <input type="checkbox" unchecked id="switch_0153"> | `enable-ndk-translation` | `kEnableNdkTranslation` | 启用使用32位NDK转换库进行ARM二进制转换。 |  |
| <input type="checkbox" unchecked id="switch_0154"> | `enable-ndk-translation64` | `kEnableNdkTranslation64` | 启用使用64位NDK转换库进行ARM二进制转换。 |  |
| <input type="checkbox" unchecked id="switch_0155"> | `enable-oobe-chromevox-hint-timer-for-dev-mode` | `kEnableOOBEChromeVoxHintForDevMode` | 在OOBE中为开发者模式启用ChromeVox提示。此标志用于覆盖禁用该功能的默认开发者模式行为。如果kEnableOOBEChromeVoxHintForDevMode和kDisableOOBEChromeVoxHintTimerForTesting都存在，ChromeVox提示将被禁用，因为后者标志优先于前者。 |  |
| <input type="checkbox" unchecked id="switch_0156"> | `enable-oobe-test-api` | `kEnableOobeTestAPI` | 为tast测试启用OOBE测试API。 |  |
| <input type="checkbox" unchecked id="switch_0157"> | `enable-requisition-edits` | `kEnableRequisitionEdits` | 启用在OOBE中配置OEM设备申请。 |  |
| <input type="checkbox" unchecked id="switch_0158"> | `enable-tablet-form-factor` | `kEnableTabletFormFactor` | 启用平板电脑外形规格。 |  |
| <input type="checkbox" unchecked id="switch_0159"> | `enable-touch-calibration-setting` | `kEnableTouchCalibrationSetting` | 为有效的触摸显示器在MD设置UI中启用触摸校准选项。 |  |
| <input type="checkbox" unchecked id="switch_0160"> | `enable-touchpad-three-finger-click` | `kEnableTouchpadThreeFingerClick` | 启用触摸板三指点击作为中键。 |  |
| <input type="checkbox" unchecked id="switch_0161"> | `enable-touchview` | `kAshEnableTabletMode` | 如果存在此标志，表示1）设备有加速度计，2）设备是可转换设备或平板设备（因此能够进入平板模式）。如果未设置此标志，则设备无法进入平板模式。例如，Samus有加速度计，但不是可转换或平板设备，因此没有设置此标志，因此无法进入平板模式。 |  |
| <input type="checkbox" unchecked id="switch_0162"> | `enable-wayland-server` | `kAshEnableWaylandServer` | 启用wayland服务器。 |  |
| <input type="checkbox" unchecked id="switch_0163"> | `enterprise-disable-arc` | `kEnterpriseDisableArc` | 为托管账户禁用ARC。 |  |
| <input type="checkbox" unchecked id="switch_0164"> | `enterprise-enable-forced-re-enrollment-on-flex` | `kEnterpriseEnableForcedReEnrollmentOnFlex` | 是否在Flex上启用强制企业重新注册。 |  |
| <input type="checkbox" unchecked id="switch_0165"> | `enterprise-enable-state-determination` | `kEnterpriseEnableUnifiedStateDetermination` | 是否启用状态确定。 |  |
| <input type="checkbox" unchecked id="switch_0166"> | `enterprise-force-manual-enrollment-in-test-builds` | `kEnterpriseForceManualEnrollmentInTestBuilds` | 是否强制手动注册而不是尝试基于证书的注册。仅在测试构建中有效。 |  |
| <input type="checkbox" unchecked id="switch_0167"> | `eol-ignore-profile-creation-time` | `kEolIgnoreProfileCreationTime` | 在确定是否显示生命周期结束通知激励时忽略配置文件创建时间。这旨在使手动测试更容易。 |  |
| <input type="checkbox" unchecked id="switch_0168"> | `eol-reset-dismissed-prefs` | `kEolResetDismissedPrefs` | 在用户会话开始时将生命周期结束通知首选项重置为默认值。这旨在使手动测试更容易。 |  |
| <input type="checkbox" unchecked id="switch_0169"> | `extension-install-event-chrome-log-for-tests` | `kExtensionInstallEventChromeLogForTests` | 将扩展安装事件写入chrome日志用于集成测试。 |  |
| <input type="checkbox" unchecked id="switch_0170"> | `external-metrics-collection-interval` | `kExternalMetricsCollectionInterval` | Chrome从/var/lib/metrics/uma-events读取外部指标之间的间隔时间（秒）。 |  |
| <input type="checkbox" unchecked id="switch_0171"> | `extra-web-apps-dir` | `kExtraWebAppsDir` | 主要外部Web应用目录的子目录名称，应从中加载其他Web应用配置。用于加载设备特定的Web应用。 |  |
| <input type="checkbox" unchecked id="switch_0172"> | `fake-arc-recommended-apps-for-testing` | `kFakeArcRecommendedAppsForTesting` | 在用户入门期间指定推荐的（虚假）ARC应用数量。应用描述在本地生成，而不是从服务器获取。仅限于ChromeOS-on-linux和测试镜像。 |  |
| <input type="checkbox" unchecked id="switch_0173"> | `fake-drivefs-launcher-chroot-path` | `kFakeDriveFsLauncherChrootPath` | 托管要使用的DriveFS的chroot的绝对路径。这仅在Linux上运行时使用，即当IsRunningOnChromeOS()返回false时。 |  |
| <input type="checkbox" unchecked id="switch_0174"> | `fake-drivefs-launcher-socket-path` | `kFakeDriveFsLauncherSocketPath` | 与kFakeDriveFsLauncherChrootPath指定的chroot内的虚假DriveFS启动器通信的套接字相对路径。这仅在Linux上运行时使用，即当IsRunningOnChromeOS()返回false时。 |  |
| <input type="checkbox" unchecked id="switch_0175"> | `fingerprint-sensor-location` | `kFingerprintSensorLocation` | 指纹传感器位置指示物理传感器的位置。值是一个字符串，可能的值包括："power-button-top-left"、"keyboard-bottom-left"、"keyboard-bottom-right"、"keyboard-top-right"。 |  |
| <input type="checkbox" unchecked id="switch_0176"> | `first-exec-after-boot` | `kFirstExecAfterBoot` | 在系统启动后第一次运行Chrome时传递给Chrome。在注销后重新启动时不传递。 |  |
| <input type="checkbox" unchecked id="switch_0177"> | `force-birch-fake-coral-backend` | `kForceBirchFakeCoralBackend` | 强制使用虚假后端生成珊瑚组。 |  |
| <input type="checkbox" unchecked id="switch_0178"> | `force-birch-fake-coral-group` | `kForceBirchFakeCoralGroup` | 强制显示带有虚假珊瑚组的芯片。 |  |
| <input type="checkbox" unchecked id="switch_0179"> | `force-birch-fetch` | `kForceBirchFetch` | 每当有信息恢复会话启动时强制获取Birch数据。 |  |
| <input type="checkbox" unchecked id="switch_0180"> | `force-birch-release-notes` | `kForceBirchReleaseNotes` | 如果设置，跳过birch发布说明提供程序中的逻辑并始终设置发布说明项。 |  |
| <input type="checkbox" unchecked id="switch_0181"> | `force-browser-data-migration-for-testing` | `kForceBrowserDataMigrationForTesting` | 强制跳过或强制迁移。仅应用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0182"> | `force-cryptohome-recovery-for-testing` | `kForceCryptohomeRecoveryForTesting` | 强制为Cryptohome恢复获取令牌。 |  |
| <input type="checkbox" unchecked id="switch_0183"> | `force-enable-stylus-tools` | `kAshForceEnableStylusTools` | 启用状态区域旁边的手写笔工具。 |  |
| <input type="checkbox" unchecked id="switch_0184"> | `force-first-run-ui` | `kForceFirstRunUI` | 强制每次登录都显示首次运行UI。 |  |
| <input type="checkbox" unchecked id="switch_0185"> | `force-happiness-tracking-system` | `kForceHappinessTrackingSystem` | 强制启用设备的幸福度跟踪系统。这忽略用户配置文件检查和时间限制，并为任何类型的用户每次都显示通知。仅应用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0186"> | `force-hwid-check-result-for-test` | `kForceHWIDCheckResultForTest` | 强制硬件ID检查（在OOBE期间发生）失败或成功。可能的值："failure"或"success"。仅应用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0187"> | `force-launch-browser` | `kForceLaunchBrowser` | 强制FullRestoreService为遥测测试启动浏览器。 |  |
| <input type="checkbox" unchecked id="switch_0188"> | `force-login-manager-in-tests` | `kForceLoginManagerInTests` | 通常在浏览器测试中会跳过常规的登录管理器启动，以便测试可以更改其启动方式。此标志禁用该功能。 |  |
| <input type="checkbox" unchecked id="switch_0189"> | `force-refresh-rate-throttle` | `kForceRefreshRateThrottle` | 在支持刷新率节流的设备上，强制节流行为处于活动状态，无论系统状态如何。 |  |
| <input type="checkbox" unchecked id="switch_0190"> | `force-show-cursor` | `kForceShowCursor` | 即使我们在模拟触摸事件，也强制显示光标。请注意，使用此开关时光标更改被锁定。 |  |
| <input type="checkbox" unchecked id="switch_0191"> | `force-show-release-track` | `kForceShowReleaseTrack` | 强制在系统托盘中显示"发布轨道"UI。模拟系统在非稳定发布渠道上并启用反馈。 |  |
| <input type="checkbox" unchecked id="switch_0192"> | `force-status-area-collapsible` | `kAshForceStatusAreaCollapsible` | 强制状态区域允许折叠/展开，无论当前状态如何。 |  |
| <input type="checkbox" unchecked id="switch_0193"> | `force-tablet-mode` | `kAshUiMode` | 为选定的UI模式启用所需功能，无论Chromebook当前是否处于选定的UI模式。 |  |
| <input type="checkbox" unchecked id="switch_0194"> | `force-tablet-power-button` | `kForceTabletPowerButton` | 如果设置，即使设备处于笔记本模式，也使用类似平板电脑的电源按钮行为（即点击按钮关闭屏幕）。 |  |
| <input type="checkbox" unchecked id="switch_0195"> | `form-factor` | `kFormFactor` | 指定设备的外形规格。如果提供，此标志覆盖LSB发布信息中的值。可能的值有："CHROMEBASE"、"CHROMEBIT"、"CHROMEBOOK"、"REFERENCE"、"CHROMEBOX" |  |
| <input type="checkbox" unchecked id="switch_0196"> | `get-access-token-for-test` | `kGetAccessTokenForTest` | 启用getAccessToken自动测试API，使用内部OAuth客户端ID创建访问令牌。 |  |
| <input type="checkbox" unchecked id="switch_0197"> | `growth-campaigns` | `kGrowthCampaigns` | 指定要覆盖用于测试的活动。 |  |
| <input type="checkbox" unchecked id="switch_0198"> | `growth-campaigns-clear-events-at-session-start` | `kGrowthCampaignsClearEventsAtSessionStart` | 在会话开始时清除所有增长框架功能参与事件，用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0199"> | `growth-campaigns-current-time` | `kGrowthCampaignsCurrentTimeSecondsSinceUnixEpoch` | 以SecondsSinceUnixEpoch格式指定设备当前时间，用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0200"> | `growth-campaigns-delayed-trigger-time-in-secs` | `kGrowthCampaignsDelayedTriggerTimeInSecs` | 指定触发活动的延迟时间，用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0201"> | `growth-campaigns-path` | `kGrowthCampaignsPath` | 用于加载增长活动文件进行测试的路径（而不是从Omaha下载）。 |  |
| <input type="checkbox" unchecked id="switch_0202"> | `growth-campaigns-registered-time` | `kGrowthCampaignsRegisteredTimeSecondsSinceUnixEpoch` | 以SecondsSinceUnixEpoch格式指定设备注册时间，用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0203"> | `guest-wallpaper-large` | `kGuestWallpaperLarge` | 在访客模式下使用的大壁纸（作为受信任的、非用户可写的JPEG文件路径）。 |  |
| <input type="checkbox" unchecked id="switch_0204"> | `guest-wallpaper-small` | `kGuestWallpaperSmall` | 在访客模式下使用的小壁纸（作为受信任的、非用户可写的JPEG文件路径）。 |  |
| <input type="checkbox" unchecked id="switch_0205"> | `has-chromeos-keyboard` | `kHasChromeOSKeyboard` | 如果设置，系统是带有"标准Chrome OS键盘"的Chromebook，通常指在Left Shift键上方的标准Caps Lock位置有搜索键的键盘。对于同时具有搜索和Caps Lock键的Chromebook（例如stout）以及仅使用外部键盘的设备（如Chromebox），应取消设置此标志。 |  |
| <input type="checkbox" unchecked id="switch_0206"> | `has-hps` | `kHasHps` | 此设备是否具有hps。 |  |
| <input type="checkbox" unchecked id="switch_0207"> | `has-internal-stylus` | `kHasInternalStylus` | 此设备是否有内置手写笔。 |  |
| <input type="checkbox" unchecked id="switch_0208"> | `has-number-pad` | `kHasNumberPad` | 如果设置，系统是带有数字键盘作为其内部键盘一部分的Chromebook。 |  |
| <input type="checkbox" unchecked id="switch_0209"> | `hidden-network-migration-age` | `kHiddenNetworkMigrationAge` | 设置错误隐藏的网络必须存在多长时间才被考虑删除。间隔应以天为单位提供，应遵循格式"--hidden-network-migration-age=#"，并且应>= 0。 |  |
| <input type="checkbox" unchecked id="switch_0210"> | `hidden-network-migration-interval` | `kHiddenNetworkMigrationInterval` | 控制HiddenNetworkHandler类检查错误隐藏网络的频率。间隔应以秒为单位提供，应遵循格式"--hidden-network-migration-interval=#"，并且应>= 1。 |  |
| <input type="checkbox" unchecked id="switch_0211"> | `homedir` | `kHomedir` | 定义用户主目录。这默认为主用户主目录。 |  |
| <input type="checkbox" unchecked id="switch_0212"> | `ignore-arcvm-dev-conf` | `kIgnoreArcVmDevConf` | 如果设置，StartArcVmRequest消息中的"ignore_dev_conf"字段将被相应设置，以便在ARCVM启动期间忽略/usr/local/vms/etc/arcvm_dev.conf中的所有开发配置指令。 |  |
| <input type="checkbox" unchecked id="switch_0213"> | `ignore-unknown-auth-factors` | `kIgnoreUnknownAuthFactors` | 如果为true，chrome将静默忽略未知的认证因子类型而不是崩溃。 |  |
| <input type="checkbox" unchecked id="switch_0214"> | `ignore-user-profile-mapping-for-tests` | `kIgnoreUserProfileMappingForTests` | 如果为true，UserManager中的配置文件选择将始终返回活动用户的配置文件。TODO(nkostlyev): http://crbug.com/364604 - 在ChromeOS上开启多配置文件功能后摆脱此开关。 |  |
| <input type="checkbox" unchecked id="switch_0215"> | `install-log-fast-upload-for-tests` | `kInstallLogFastUploadForTests` | 减少集成测试上传安装事件日志的延迟。 |  |
| <input type="checkbox" unchecked id="switch_0216"> | `kiosk-splash-screen-min-time-seconds` | `kKioskSplashScreenMinTimeSeconds` | 信息亭启动画面将显示的最短时间（秒）。 |  |
| <input type="checkbox" unchecked id="switch_0217"> | `launch-rma` | `kLaunchRma` | 在RMA模式下启动Chrome。自动启动RMA应用。kRmaNotAllowed开关优先于此开关。 |  |
| <input type="checkbox" unchecked id="switch_0218"> | `lobster-feature-key` | `kLobsterFeatureKey` | 启用lobster功能。 |  |
| <input type="checkbox" unchecked id="switch_0219"> | `localhost` | `kPrintingPpdChannelLocalhost` |  |  |
| <input type="checkbox" unchecked id="switch_0220"> | `login-manager` | `kLoginManager` | 启用Chrome作为登录管理器的行为。 |  |
| <input type="checkbox" unchecked id="switch_0221"> | `login-profile` | `kLoginProfile` | 指定chromeos用户登录后要使用的配置文件。如果用户通过登录屏幕，此参数将被忽略，因为user_id哈希定义了要使用的配置文件目录。在活动会话中浏览器重新启动的情况下，此参数用于传递主用户的user_id哈希。 |  |
| <input type="checkbox" unchecked id="switch_0222"> | `login-user` | `kLoginUser` | 指定已经登录的用户。 |  |
| <input type="checkbox" unchecked id="switch_0223"> | `mall-url` | `kMallUrl` | 应用商城的基础URL。 |  |
| <input type="checkbox" unchecked id="switch_0224"> | `mantis-feature-key` | `kMantisFeatureKey` | 提供Mantis功能的密钥。 |  |
| <input type="checkbox" unchecked id="switch_0225"> | `marketing-opt-in-url` | `kMarketingOptInUrl` | 确定调用后端时要使用的URL。 |  |
| <input type="checkbox" unchecked id="switch_0226"> | `note-taking-app-ids` | `kNoteTakingAppIds` | 可用于记笔记的应用ID的可选逗号分隔列表。如果未设置，则使用硬编码列表。 |  |
| <input type="checkbox" unchecked id="switch_0227"> | `oobe-disable-pre-consent-metrics-for-testing` | `kOobeDisablePreConsentMetricsForTesting` | 禁用测试的指标同意。 |  |
| <input type="checkbox" unchecked id="switch_0228"> | `oobe-eula-url-for-tests` | `kOobeEulaUrlForTests` | 允许为测试覆盖eula url。 |  |
| <input type="checkbox" unchecked id="switch_0229"> | `oobe-force-tablet-first-run` | `kOobeForceTabletFirstRun` | 指示首次用户运行流程（首次用户登录后的OOBE屏幕序列）应显示平板模式为中心的屏幕，即使设备不在平板模式。 |  |
| <input type="checkbox" unchecked id="switch_0230"> | `oobe-large-screen-special-scaling` | `kOobeLargeScreenSpecialScaling` | 指示OOBE应该为大显示器缩放，类似于Meets应用缩放UI的方式。TODO(crbug.com/1205364): 添加新方案后删除。 |  |
| <input type="checkbox" unchecked id="switch_0231"> | `oobe-print-frontend-load-timings` | `kOobePrintFrontendLoadTimings` | 存在时，打印OOBE前端加载所需的时间。详情见go/oobe-frontend-trace-timings。 |  |
| <input type="checkbox" unchecked id="switch_0232"> | `oobe-screenshot-dir` | `kOobeScreenshotDirectory` | 指定使用OOBE UI调试器拍摄的屏幕截图目录。 |  |
| <input type="checkbox" unchecked id="switch_0233"> | `oobe-show-accessibility-button-on-marketing-opt-in-for-testing` | `kOobeShowAccessibilityButtonOnMarketingOptInForTesting` | 在营销选择加入时显示a11y按钮，而不访问手势导航屏幕。 |  |
| <input type="checkbox" unchecked id="switch_0234"> | `oobe-skip-network-setup-for-testing` | `kOOBESkipNetworkSetupForTesting` | 即使没有互联网连接也跳过OOBE网络设置。 |  |
| <input type="checkbox" unchecked id="switch_0235"> | `oobe-skip-new-user-check-for-testing` | `kOobeSkipNewUserCheckForTesting` | 在个性化推荐应用屏幕中跳过新用户检查以进行测试。 |  |
| <input type="checkbox" unchecked id="switch_0236"> | `oobe-skip-postlogin` | `kOobeSkipPostLogin` | 跳过用户登录后的所有其他OOBE页面。 |  |
| <input type="checkbox" unchecked id="switch_0237"> | `oobe-skip-split-modifier-check-for-testing` | `kOobeSkipSplitModifierCheckForTesting` | 如果我们应该在分离修饰键信息屏幕上跳过分离修饰键检查，则返回true。 |  |
| <input type="checkbox" unchecked id="switch_0238"> | `oobe-skip-to-login` | `kOobeSkipToLogin` | 跳转到登录屏幕。 |  |
| <input type="checkbox" unchecked id="switch_0239"> | `oobe-timer-interval` | `kOobeTimerInterval` | 检查OOBE总时间的间隔。 |  |
| <input type="checkbox" unchecked id="switch_0240"> | `oobe-timezone-override-for-tests` | `kOobeTimezoneOverrideForTests` | 允许在营销选择加入屏幕上覆盖时区。 |  |
| <input type="checkbox" unchecked id="switch_0241"> | `oobe-trigger-sync-timeout-for-tests` | `kOobeTriggerSyncTimeoutForTests` | 在OOBE中触发同步引擎初始化超时进行测试。 |  |
| <input type="checkbox" unchecked id="switch_0242"> | `overscan-insets-override` | `kOverscanInsetsOverride` | 如果设置，覆盖所有显示器的过扫描设置。 |  |
| <input type="checkbox" unchecked id="switch_0243"> | `overview-button-for-tests` | `kOverviewButtonForTests` | 如果设置，概览按钮将可见。 |  |
| <input type="checkbox" unchecked id="switch_0244"> | `performance` | `kSchedulerConfigurationPerformance` |  |  |
| <input type="checkbox" unchecked id="switch_0245"> | `prevent-kiosk-autolaunch-for-testing` | `kPreventKioskAutolaunchForTesting` | 防止信息亭自动启动进行测试。 |  |
| <input type="checkbox" unchecked id="switch_0246"> | `printing-ppd-channel` | `kPrintingPpdChannel` | 设置加载PPD文件的通道。 |  |
| <input type="checkbox" unchecked id="switch_0247"> | `privacy-policy-host-for-tests` | `kPrivacyPolicyHostForTests` | 设置测试用的隐私政策主机名url。 |  |
| <input type="checkbox" unchecked id="switch_0248"> | `production` | `kPrintingPpdChannelProduction` |  |  |
| <input type="checkbox" unchecked id="switch_0249"> | `profile-requires-policy` | `kProfileRequiresPolicy` | 如果设置为"true"，配置文件在重新启动期间需要策略（策略加载必须成功，否则会话重新启动应该失败）。 |  |
| <input type="checkbox" unchecked id="switch_0250"> | `public-accounts-saml-acl-url` | `kPublicAccountsSamlAclUrl` | SAML断言消费者URL，用于检测Gaia-less SAML流程何时结束（例如SAML托管访客会话）TODO(crbug.com/40636049): 当DMServer发送URL时删除。 |  |
| <input type="checkbox" unchecked id="switch_0251"> | `qs-add-fake-bluetooth-devices` | `kQsAddFakeBluetoothDevices` | 向快速设置菜单添加虚假蓝牙设备进行UI测试。 |  |
| <input type="checkbox" unchecked id="switch_0252"> | `qs-add-fake-cast-devices` | `kQsAddFakeCastDevices` | 向快速设置菜单添加虚假Cast设备进行UI测试。 |  |
| <input type="checkbox" unchecked id="switch_0253"> | `qs-show-locale-tile` | `kQsShowLocaleTile` | 强制显示快速设置"locale"功能磁贴。通常它只在演示模式下显示，在模拟器中不工作。 |  |
| <input type="checkbox" unchecked id="switch_0254"> | `regulatory-label-dir` | `kRegulatoryLabelDir` | 包含此模型监管标签文件的每区域子目录的每模型目录名称。每模型目录（如果有）位于"/usr/share/chromeos-assets/regulatory_labels/"下。 |  |
| <input type="checkbox" unchecked id="switch_0255"> | `remote-reboot-command-timeout-in-seconds-for-testing` | `kRemoteRebootCommandDelayInSecondsForTesting` | 重启命令的测试延迟。对tast测试有用。 |  |
| <input type="checkbox" unchecked id="switch_0256"> | `reven-branding` | `kRevenBranding` | 指示应显示reven UI字符串和功能。 |  |
| <input type="checkbox" unchecked id="switch_0257"> | `rlz-ping-delay` | `kRlzPingDelay` | 覆盖默认值的rlz ping延迟（以秒为单位）。 |  |
| <input type="checkbox" unchecked id="switch_0258"> | `rma-not-allowed` | `kRmaNotAllowed` | 启动Chrome而不打开RMA或检查当前RMA状态。 |  |
| <input type="checkbox" unchecked id="switch_0259"> | `safe-mode` | `kSafeMode` | 当chrome在启动的前60秒内崩溃3次或更多次时，由session_manager守护程序添加的开关。参见platform2/login_manager/browser_job.cc中的BrowserJob::ExportArgv。 |  |
| <input type="checkbox" unchecked id="switch_0260"> | `saml-password-change-url` | `kSamlPasswordChangeUrl` | SAML用户的密码更改url。TODO(crbug.com/40618074): 修复错误后删除。 |  |
| <input type="checkbox" unchecked id="switch_0261"> | `scheduled-reboot-grace-period-in-seconds-for-testing` | `kScheduledRebootGracePeriodInSecondsForTesting` | DeviceScheduledReboot策略的测试宽限期。对tast测试有用。参见scheduled_task_util.h中的ShouldSkipRebootDueToGracePeriod。 |  |
| <input type="checkbox" unchecked id="switch_0262"> | `scheduler-configuration` | `kSchedulerConfiguration` | 选择参数中指定的调度器配置。 |  |
| <input type="checkbox" unchecked id="switch_0263"> | `scheduler-configuration-default` | `kSchedulerConfigurationDefault` | 如果用户未设置调度器配置，指定默认调度器配置值是什么。 |  |
| <input type="checkbox" unchecked id="switch_0264"> | `shelf-hotseat` | `kShelfHotseat` | 货架的新模块化设计，在翻盖模式下将应用分离到hotseat UI和较小货架中。 |  |
| <input type="checkbox" unchecked id="switch_0265"> | `show-login-dev-overlay` | `kShowLoginDevOverlay` | 如果为true，将为登录/锁屏显示开发者工具覆盖。这使测试布局逻辑更容易。 |  |
| <input type="checkbox" unchecked id="switch_0266"> | `show-oobe-dev-overlay` | `kShowOobeDevOverlay` | 启用OOBE UI调试器，便于在手动测试期间在屏幕之间导航。仅限于ChromeOS-on-linux和测试镜像。 |  |
| <input type="checkbox" unchecked id="switch_0267"> | `show-oobe-quick-start-debugger` | `kShowOobeQuickStartDebugger` | 在OOBE中启用QuickStart调试器，模拟Android手机。 |  |
| <input type="checkbox" unchecked id="switch_0268"> | `show-taps` | `kShowTaps` | 在每个触摸点绘制圆圈，类似于Android OS开发者选项"显示触摸"。 |  |
| <input type="checkbox" unchecked id="switch_0269"> | `skip-force-online-signin-for-testing` | `kSkipForceOnlineSignInForTesting` | 在tast测试中禁用在线登录强制执行。 |  |
| <input type="checkbox" unchecked id="switch_0270"> | `skip-multidevice-screen` | `kSkipMultideviceScreenForTesting` | 在tast测试期间跳过多设备设置屏幕。 |  |
| <input type="checkbox" unchecked id="switch_0271"> | `skip-reorder-nudge-show-threshold-duration` | `kSkipReorderNudgeShowThresholdDurationForTest` | 用于跳过重新排序提示必须显示的阈值持续时间，然后该提示才被视为已显示。 |  |
| <input type="checkbox" unchecked id="switch_0272"> | `stabilize-time-dependent-view-for-tests` | `kStabilizeTimeDependentViewForTests` | 如果为true，时间相关视图（如时间视图）显示预定义的固定时间。 |  |
| <input type="checkbox" unchecked id="switch_0273"> | `staging` | `kPrintingPpdChannelStaging` |  |  |
| <input type="checkbox" unchecked id="switch_0274"> | `supports-clamshell-auto-rotation` | `kSupportsClamshellAutoRotation` | 如果设置，设备将被强制保持在翻盖UI模式，但将支持屏幕自动旋转。例如，chromebase设备Dooly。 |  |
| <input type="checkbox" unchecked id="switch_0275"> | `suppress-message-center-popups` | `kSuppressMessageCenterPopups` | 隐藏所有消息中心通知弹出窗口（toast）。用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0276"> | `telemetry-extension-dir` | `kTelemetryExtensionDirectory` | 指定遥测系统Web扩展的目录。 |  |
| <input type="checkbox" unchecked id="switch_0277"> | `test-encryption-migration-ui` | `kTestEncryptionMigrationUI` | 启用加密迁移UI测试。 |  |
| <input type="checkbox" unchecked id="switch_0278"> | `test-wallpaper-server` | `kTestWallpaperServer` | 启用壁纸选择器从测试服务器获取图像。 |  |
| <input type="checkbox" unchecked id="switch_0279"> | `tether-host-scans-ignore-wired-connections` | `kTetherHostScansIgnoreWiredConnections` | 告诉Chromebook扫描网络共享主机，即使已有有线连接。这允许通过以太网部署端到端测试，而不会因该连接阻止扫描，从而阻止测试无预先存在连接的情况。应仅用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0280"> | `tether-stub` | `kTetherStub` | 用存根服务覆盖Tether。为所需的虚假网络数量提供整数参数，例如'tether-stub=2'。 |  |
| <input type="checkbox" unchecked id="switch_0281"> | `time-before-onboarding-survey-in-seconds-for-testing` | `kTimeBeforeOnboardingSurveyInSecondsForTesting` | 用于覆盖运行入门调查前所需的用户活动时间。 |  |
| <input type="checkbox" unchecked id="switch_0282"> | `touch_view` | `kAshUiModeTablet` |  |  |
| <input type="checkbox" unchecked id="switch_0283"> | `touchscreen-usable-while-screen-off` | `kTouchscreenUsableWhileScreenOff` | Chromebases的触摸屏可用于从挂起状态唤醒，不像其他Chrome OS设备上的触摸屏。如果设置，在屏幕关闭时保持触摸屏启用，以便在因不活动而关闭屏幕后但在系统挂起前，可以使用它重新开启屏幕。 |  |
| <input type="checkbox" unchecked id="switch_0284"> | `tpm-is-dynamic` | `kTpmIsDynamic` | 在运行时启用TPM选择。 |  |
| <input type="checkbox" unchecked id="switch_0285"> | `unfiltered-bluetooth-devices` | `kUnfilteredBluetoothDevices` | 在UI（系统托盘/设置页面）中显示所有蓝牙设备。 |  |
| <input type="checkbox" unchecked id="switch_0286"> | `use-fake-cras-audio-client-for-dbus` | `kUseFakeCrasAudioClientForDBus` | 使用虚假的FakeCrasAudioClient处理系统音频控制。 |  |
| <input type="checkbox" unchecked id="switch_0287"> | `use-myfiles-in-user-data-dir-for-testing` | `kUseMyFilesInUserDataDirForTesting` | 标志，将MyFiles文件夹存储在用户数据目录中。$HOME/Downloads在Linux运行时用作MyFiles文件夹以便于访问本地文件进行调试。通过设置此标志，即使在Linux上也使用<cryptohome>/MyFiles。 |  |
| <input type="checkbox" unchecked id="switch_0288"> | `web-ui-data-source-path-for-testing` | `kWebUiDataSourcePathForTesting` | 如果提供，任何webui将从<flag value>/<handler_name>加载，其中handler_name是传递给MaybeConfigureTestableDataSource的名称（如果文件存在）。例如，如果标志是/tmp/resource_overrides，尝试从名为"help_app/untrusted"的数据源加载js/app_main.js将首先尝试从/tmp/resource_overrides/help_app/untrusted/js/main.js加载。 |  |

## Ash Constants Ash Switches.h (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0289"> | `force-browser-data-backward-migration` | `kForceBrowserDataBackwardMigration` |  |  |

## Assistant (3 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0290"> | `disable-libassistant-logfile` | `kDisableLibAssistantLogfile` | 禁用libassistant日志文件。 |  |
| <input type="checkbox" unchecked id="switch_0291"> | `force-assistant-onboarding` | `kForceAssistantOnboarding` | 强制助手入门流程。 |  |
| <input type="checkbox" unchecked id="switch_0292"> | `redirect-libassistant-logging` | `kRedirectLibassistantLogging` | 重定向libassistant日志记录。 |  |

## Autofill (7 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0293"> | `autofill-api-key` | `kAutofillAPIKey` | 设置调用Autofill API时使用的API密钥，而不是默认使用Chrome的内置密钥。您可以使用此功能测试尚未链接到Chrome内置密钥的API新版本。 |  |
| <input type="checkbox" unchecked id="switch_0294"> | `autofill-server-url` | `kAutofillServerURL` | 用"scheme://host[:port]/prefix/"覆盖默认的自动填充服务器URL。 |  |
| <input type="checkbox" unchecked id="switch_0295"> | `autofill-upload-throttling-period-in-days` | `kAutofillUploadThrottlingPeriodInDays` | 重置已发送上传的自动填充事件注册表前的天数。 |  |
| <input type="checkbox" unchecked id="switch_0296"> | `ignore-autocomplete-off-autofill` | `kIgnoreAutocompleteOffForAutofill` | 忽略Autofill数据（配置文件+信用卡）的autocomplete="off"属性。 |  |
| <input type="checkbox" unchecked id="switch_0297"> | `show-autofill-signatures` | `kShowAutofillSignatures` | 用Autofill签名标注表单和字段。 |  |
| <input type="checkbox" unchecked id="switch_0298"> | `show-autofill-type-predictions` | `kShowAutofillTypePredictions` | 用Autofill字段类型预测标注表单。 |  |
| <input type="checkbox" unchecked id="switch_0299"> | `wallet-service-use-sandbox` | `kWalletServiceUseSandbox` | 使用沙盒Online Wallet服务URL（用于开发者测试）。 |  |

## Borealis (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0300"> | `borealis-launch-options` | `kLaunchOptions` | 允许向chrome进程传递BorealisLaunchOptions字符串，该字符串将存储在kExtraLaunchOptions中。有关格式，请参阅chrome/browser/ash/borealis/borealis_launch_options.h中的文档。 |  |

## CC (32 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0301"> | `cc-layer-tree-test-long-timeout` | `kCCLayerTreeTestLongTimeout` | 增加内存检查器的超时时间。 |  |
| <input type="checkbox" unchecked id="switch_0302"> | `cc-layer-tree-test-no-timeout` | `kCCLayerTreeTestNoTimeout` | 防止图层树单元测试超时。 |  |
| <input type="checkbox" unchecked id="switch_0303"> | `cc-scroll-animation-duration-in-seconds` | `kCCScrollAnimationDurationForTesting` | 控制滚动动画曲线的持续时间。 |  |
| <input type="checkbox" unchecked id="switch_0304"> | `check-damage-early` | `kCheckDamageEarly` | 提前检查损坏并在无损坏时中止帧，以便像Android WebView这样的客户端不会不必要地失效。 |  |
| <input type="checkbox" unchecked id="switch_0305"> | `disable-checker-imaging` | `kDisableCheckerImaging` | 禁用将所有图像解码延迟到图像解码服务，忽略在PaintImage上指定的DecodingMode首选项。 |  |
| <input type="checkbox" unchecked id="switch_0306"> | `disable-composited-antialiasing` | `kDisableCompositedAntialiasing` | 在合成器中禁用图层边缘抗锯齿。 |  |
| <input type="checkbox" unchecked id="switch_0307"> | `disable-layer-tree-host-memory-pressure` | `kDisableLayerTreeHostMemoryPressure` | 禁用LayerTreeHost::OnMemoryPressure。 |  |
| <input type="checkbox" unchecked id="switch_0308"> | `disable-main-frame-before-activation` | `kDisableMainFrameBeforeActivation` | 禁用在前一个提交激活之前发送下一个BeginMainFrame。覆盖kEnableMainFrameBeforeActivation标志。 |  |
| <input type="checkbox" unchecked id="switch_0309"> | `disable-threaded-animation` | `kDisableThreadedAnimation` | 禁用多线程动画。 |  |
| <input type="checkbox" unchecked id="switch_0310"> | `enable-gpu-benchmarking` | `kEnableGpuBenchmarking` | 启用GPU基准测试扩展。 |  |
| <input type="checkbox" unchecked id="switch_0311"> | `enable-main-frame-before-activation` | `kEnableMainFrameBeforeActivation` | 启用在前一个提交激活之前发送下一个BeginMainFrame。 |  |
| <input type="checkbox" unchecked id="switch_0312"> | `enable-scaling-clipped-images` | `kEnableClippedImageScaling` | 允许在GpuImageDecodeCache中缩放裁剪图像。注意，这可能导致颜色出血。TODO(crbug.com/40160880)：一旦底层缓存问题得到解决，请删除此变通标志。 |  |
| <input type="checkbox" unchecked id="switch_0313"> | `highlight-non-lcd-text-layers` | `kHighlightNonLCDTextLayers` | 突出显示不能使用LCD文本的图层。不包含文本的图层不会被突出显示。有关颜色，请参阅DebugColors::NonLCDTextHighlightColor()。 |  |
| <input type="checkbox" unchecked id="switch_0314"> | `layer` | `kCompositedLayerBorders` | 合成图层边框参数。 |  |
| <input type="checkbox" unchecked id="switch_0315"> | `num-raster-threads` | `kNumRasterThreads` | 控制用于栅格化任务的线程数。 |  |
| <input type="checkbox" unchecked id="switch_0316"> | `renderpass` | `kCompositedRenderPassBorders` | kUIShowCompositedLayerBorders的参数。 |  |
| <input type="checkbox" unchecked id="switch_0317"> | `show-composited-layer-borders` | `kShowCompositedLayerBorders` | 在合成器图层周围渲染边框，以帮助调试和研究图层合成。 |  |
| <input type="checkbox" unchecked id="switch_0318"> | `show-fps-counter` | `kShowFPSCounter` | 绘制显示每秒帧数以及GPU内存使用情况的抬头显示。如果您还使用--enable-logging=stderr --vmodule="head*=1"，那么FPS也将输出到控制台日志中。 |  |
| <input type="checkbox" unchecked id="switch_0319"> | `show-layer-animation-bounds` | `kShowLayerAnimationBounds` | 渲染表示图层动画边界框的边框。 |  |
| <input type="checkbox" unchecked id="switch_0320"> | `show-property-changed-rects` | `kShowPropertyChangedRects` | 在HUD中显示属性已更改图层周围的矩形。 |  |
| <input type="checkbox" unchecked id="switch_0321"> | `show-screenspace-rects` | `kShowScreenSpaceRects` | 在HUD中显示每个图层屏幕空间变换边界周围的矩形。 |  |
| <input type="checkbox" unchecked id="switch_0322"> | `show-surface-damage-rects` | `kShowSurfaceDamageRects` | 在HUD中显示损坏记录到每个渲染表面时的矩形。 |  |
| <input type="checkbox" unchecked id="switch_0323"> | `slow-down-raster-scale-factor` | `kSlowDownRasterScaleFactor` | 多次重新栅格化所有内容以模拟更慢的机器。提供缩放因子使栅格化完成时间增加相应倍数，例如--slow-down-raster-scale-factor=25。 |  |
| <input type="checkbox" unchecked id="switch_0324"> | `surface` | `kCompositedSurfaceBorders` | 合成表面边框参数。 |  |
| <input type="checkbox" unchecked id="switch_0325"> | `top-controls-hide-threshold` | `kBrowserControlsHideThreshold` | 浏览器控件需要隐藏的百分比，超过此值将自动隐藏。 |  |
| <input type="checkbox" unchecked id="switch_0326"> | `top-controls-show-threshold` | `kBrowserControlsShowThreshold` | 浏览器控件需要显示的百分比，超过此值将自动显示。 |  |
| <input type="checkbox" unchecked id="switch_0327"> | `ui-show-composited-layer-borders` | `kUIShowCompositedLayerBorders` | UI显示合成图层边框。 |  |
| <input type="checkbox" unchecked id="switch_0328"> | `ui-show-fps-counter` | `kUIShowFPSCounter` | UI显示FPS计数器。 |  |
| <input type="checkbox" unchecked id="switch_0329"> | `ui-show-layer-animation-bounds` | `kUIShowLayerAnimationBounds` | UI显示图层动画边界。 |  |
| <input type="checkbox" unchecked id="switch_0330"> | `ui-show-property-changed-rects` | `kUIShowPropertyChangedRects` | UI显示属性更改矩形。 |  |
| <input type="checkbox" unchecked id="switch_0331"> | `ui-show-screenspace-rects` | `kUIShowScreenSpaceRects` | UI显示屏幕空间矩形。 |  |
| <input type="checkbox" unchecked id="switch_0332"> | `ui-show-surface-damage-rects` | `kUIShowSurfaceDamageRects` | UI显示表面损坏矩形。 |  |

## Chrome Browser Ash Android Sms Android Sms Switches.cc (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0333"> | `custom-android-messages-domain` | `kCustomAndroidMessagesDomain` | 自定义Android Messages域名。 |  |

## Chrome Browser Google Switches.cc (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0334"> | `simulate-update-error-code` | `kSimulateUpdateErrorCode` | 通过更新检查模拟GoogleUpdateErrorCode错误。必须与\|kSimulateUpdateHresult\|开关一起提供。 |  |
| <input type="checkbox" unchecked id="switch_0335"> | `simulate-update-hresult` | `kSimulateUpdateHresult` | 模拟更新检查返回的特定HRESULT错误代码。如果未指定开关值（以十六进制），则默认为E_FAIL。 |  |

## Chrome Browser Ip Protection Ip Protection Switches.cc (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0336"> | `disable-ip-privacy-proxy` | `kDisableIpProtectionProxy` | 禁用IP隐私保护代理。 |  |

## Chrome Browser Nearby Sharing Nearby Share Switches.cc (5 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0337"> | `nearby-share-certificate-validity-period-hours` | `kNearbyShareCertificateValidityPeriodHours` | 覆盖Nearby Share证书的默认有效期。值必须大于0。 |  |
| <input type="checkbox" unchecked id="switch_0338"> | `nearby-share-device-id` | `kNearbyShareDeviceID` | 覆盖默认设备ID，在测试环境中提供稳定的ID。默认情况下，我们生成一个随机的10字符字符串。 |  |
| <input type="checkbox" unchecked id="switch_0339"> | `nearby-share-num-private-certificates` | `kNearbyShareNumPrivateCertificates` | 覆盖生成的私人证书的默认数量。值必须大于0。 |  |
| <input type="checkbox" unchecked id="switch_0340"> | `nearby-share-verbose-logging` | `kNearbyShareVerboseLogging` | 启用Nearby Share的详细日志记录级别。 |  |
| <input type="checkbox" unchecked id="switch_0341"> | `nearbysharing-http-host` | `kNearbyShareHTTPHost` | 覆盖Nearby Share使用的默认Google APIs URL (https://www.googleapis.com)。 |  |

## Chrome Chrome Switches.cc (154 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0342"> | `allow-cross-origin-auth-prompt` | `kAllowCrossOriginAuthPrompt` | 允许页面上包含的第三方内容提示HTTP基本身份验证用户名/密码对。 |  |
| <input type="checkbox" unchecked id="switch_0343"> | `allow-http-screen-capture` | `kAllowHttpScreenCapture` | 允许非安全来源使用屏幕捕获API和desktopCapture扩展API。 |  |
| <input type="checkbox" unchecked id="switch_0344"> | `allow-running-insecure-content` | `kAllowRunningInsecureContent` | 默认情况下，https页面不能运行来自http URL的JavaScript、CSS或插件。这提供了一个覆盖选项来获取旧的不安全行为。 |  |
| <input type="checkbox" unchecked id="switch_0345"> | `allow-silent-push` | `kAllowSilentPush` | 允许不显示通知的Web Push通知。 |  |
| <input type="checkbox" unchecked id="switch_0346"> | `app` | `kApp` | 指定关联的值应在"应用程序"模式下启动。 |  |
| <input type="checkbox" unchecked id="switch_0347"> | `app-id` | `kAppId` | 指定具有指定ID的扩展应用应按照其配置启动。 |  |
| <input type="checkbox" unchecked id="switch_0348"> | `app-launch-url-for-shortcuts-menu-item` | `kAppLaunchUrlForShortcutsMenuItem` | 用指定URL覆盖应用的启动URL。这与kAppId一起使用，用对应应用快捷菜单中项目的URL启动给定应用。 |  |
| <input type="checkbox" unchecked id="switch_0349"> | `app-mode-auth-code` | `kAppModeAuthCode` | --force-app-mode的GAIA身份验证代码值。 |  |
| <input type="checkbox" unchecked id="switch_0350"> | `app-mode-oauth-token` | `kAppModeOAuth2Token` | --force-app-mode的OAuth2刷新令牌值。 |  |
| <input type="checkbox" unchecked id="switch_0351"> | `app-run-on-os-login-mode` | `kAppRunOnOsLoginMode` | 与kAppId一起使用，指示应用在OS登录期间启动，以及应用以何种模式启动。 |  |
| <input type="checkbox" unchecked id="switch_0352"> | `apps-gallery-download-url` | `kAppsGalleryDownloadURL` | 覆盖webstore API下载扩展的URL。注意：URL必须包含一个'%s'用于扩展ID。 |  |
| <input type="checkbox" unchecked id="switch_0353"> | `apps-gallery-update-url` | `kAppsGalleryUpdateURL` | 覆盖webstore扩展使用的更新URL。 |  |
| <input type="checkbox" unchecked id="switch_0354"> | `apps-gallery-url` | `kAppsGalleryURL` | 覆盖浏览器视为webstore的URL，授予其webstore API并给予一些特殊保护。 |  |
| <input type="checkbox" unchecked id="switch_0355"> | `auto-accept-browser-signin-for-tests` | `kBrowserSigninAutoAccept` | 在网络上登录其他Google服务时自动将用户登录Chrome。这使得自动化浏览器更容易登录。 |  |
| <input type="checkbox" unchecked id="switch_0356"> | `auto-accept-this-tab-capture` | `kThisTabCaptureAutoAccept` | 这些标志使Chrome自动接受/拒绝捕获当前标签页的请求。它应该仅用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0357"> | `auto-open-devtools-for-tabs` | `kAutoOpenDevToolsForTabs` | 此标志使Chrome为每个标签页自动打开DevTools窗口。它旨在供开发人员和自动化使用，无需用户交互即可打开DevTools。 |  |
| <input type="checkbox" unchecked id="switch_0358"> | `auto-reject-capture` | `kCaptureAutoReject` | 此标志使Chrome自动拒绝捕获标签页/窗口/屏幕的请求。 |  |
| <input type="checkbox" unchecked id="switch_0359"> | `auto-reject-this-tab-capture` | `kThisTabCaptureAutoReject` | 自动拒绝此标签页捕获。 |  |
| <input type="checkbox" unchecked id="switch_0360"> | `auto-select-desktop-capture-source` | `kAutoSelectDesktopCaptureSource` | 此标志使Chrome在扩展请求开始桌面捕获权限时自动选择提供的选项。应仅用于测试。例如，--auto-select-desktop-capture-source="Entire screen"将在英语环境中自动选择共享整个屏幕。开关值只需要是捕获源名称的子字符串，即"display"将匹配"Built-in display"和"External display"，以先出现的为准。 |  |
| <input type="checkbox" unchecked id="switch_0361"> | `auto-select-screen-capture-source` | `kAutoSelectScreenCaptureSource` | 此标志使Chrome在扩展请求开始桌面捕获权限时自动选择任何屏幕。应仅用于测试。kAutoSelectDesktopCaptureSource（见上文）也可用于自动选择屏幕。但它有一个问题，你需要知道屏幕的名称才能自动选择它。屏幕的名称无法设置，在不同平台上不同，如果你有一个或多个屏幕也会不同。所以很难用于自动选择屏幕。此标志不关心屏幕名称是什么，但也不提供控制。可以选择任何屏幕。在我们不关心自动选择哪个屏幕的测试中很有用。 |  |
| <input type="checkbox" unchecked id="switch_0362"> | `auto-select-tab-capture-source-by-title` | `kAutoSelectTabCaptureSourceByTitle` | 此标志使Chrome在应该向用户显示媒体选择器时自动选择具有提供标题的标签页。此开关与kAutoSelectDesktopCaptureSource非常相似，但将选择限制为标签页。这解决了kAutoSelectDesktopCaptureSource可能意外捕获Chromium窗口而不是标签页的问题，因为如果标签页处于焦点状态，两者具有相同的标题。 |  |
| <input type="checkbox" unchecked id="switch_0363"> | `auto-select-window-capture-source-by-title` | `kAutoSelectWindowCaptureSourceByTitle` | 此标志使Chrome在应该向用户显示媒体选择器时自动选择具有提供标题的窗口。此开关与kAutoSelectDesktopCaptureSource非常相似，但将选择限制为窗口。 |  |
| <input type="checkbox" unchecked id="switch_0364"> | `bootstrap` | `kExtensionContentVerificationBootstrap` | kExtensionContentVerification标志的值。有关更多说明，请参见ContentVerifierDelegate::Mode。 |  |
| <input type="checkbox" unchecked id="switch_0365"> | `bypass-account-already-used-by-another-profile-check` | `kBypassAccountAlreadyUsedByAnotherProfileCheck` | 如果指定，允许将多个配置文件同步到同一帐户。用于多客户端端到端测试。 |  |
| <input type="checkbox" unchecked id="switch_0366"> | `cast-mirroring-target-playout-delay` | `kCastMirroringTargetPlayoutDelay` | 如果启用，覆盖投射镜像会话的目标播放延迟。该值将解析为毫秒。降低此值将导致更低的端到端延迟，但可能以其他质量标准为代价，如丢帧或FPS。 |  |
| <input type="checkbox" unchecked id="switch_0367"> | `check-for-update-interval` | `kCheckForUpdateIntervalSec` | 检查更新的频率（以秒为单位）。应仅用于测试目的。 |  |
| <input type="checkbox" unchecked id="switch_0368"> | `cipher-suite-blacklist` | `kCipherSuiteBlacklist` | 要禁用的SSL密码套件的逗号分隔列表。 |  |
| <input type="checkbox" unchecked id="switch_0369"> | `crash-on-hang-threads` | `kCrashOnHangThreads` | 如果给定的浏览器线程无响应，导致浏览器进程崩溃的BrowserThreads的逗号分隔列表。支持UI/IO BrowserThreads。例如：--crash-on-hang-threads=UI:18,IO:18 --> 如果UI或IO在其他浏览器线程响应的情况下18秒无响应，则使浏览器崩溃。 |  |
| <input type="checkbox" unchecked id="switch_0370"> | `create-browser-on-startup-for-tests` | `kCreateBrowserOnStartupForTests` | 某些平台（如ChromeOS）默认为空桌面。浏览器测试可能需要添加此开关，以便在启动时至少创建一个浏览器实例。TODO(nkostylev)：调查是否可以删除此开关。(http://crbug.com/148675) |  |
| <input type="checkbox" unchecked id="switch_0371"> | `create-profile-email-if-not-exists` | `kCreateProfileEmailIfNotExists` | 如果与kProfileEmail一起提供，在任何现有配置文件中未找到该电子邮件时，提示用户创建以kProfileEmail作为电子邮件地址的新配置文件。 |  |
| <input type="checkbox" unchecked id="switch_0372"> | `credits` | `kCredits` | 打印许可信息（与about:credits中的内容相同）并退出。 |  |
| <input type="checkbox" unchecked id="switch_0373"> | `custom-devtools-frontend` | `kCustomDevtoolsFrontend` | 指定将用于提供devtools://devtools/custom/<path>的http://端点，或指定用于从devtools://devtools/bundled/<path>加载的自定义文件路径的file:// URL。 |  |
| <input type="checkbox" unchecked id="switch_0374"> | `debug-packed-apps` | `kDebugPackedApps` | 向打包应用的上下文菜单添加调试条目，如检查元素。 |  |
| <input type="checkbox" unchecked id="switch_0375"> | `devtools-flags` | `kDevToolsFlags` | 向DevTools前端传递命令行参数。 |  |
| <input type="checkbox" unchecked id="switch_0376"> | `diagnostics` | `kDiagnostics` | 触发大量诊断模式。 |  |
| <input type="checkbox" unchecked id="switch_0377"> | `diagnostics-format` | `kDiagnosticsFormat` | 设置由诊断标志启用的诊断模式的输出格式。 |  |
| <input type="checkbox" unchecked id="switch_0378"> | `diagnostics-recovery` | `kDiagnosticsRecovery` | 告诉诊断模式执行请求的恢复步骤。 |  |
| <input type="checkbox" unchecked id="switch_0379"> | `disable-background-networking` | `kDisableBackgroundNetworking` | 禁用在后台运行网络请求的几个子系统。这用于进行网络性能测试时避免测量中的噪声。 |  |
| <input type="checkbox" unchecked id="switch_0380"> | `disable-component-extensions-with-background-pages` | `kDisableComponentExtensionsWithBackgroundPages` | 禁用具有后台页面的默认组件扩展 - 对于这些页面可能干扰性能结果的性能测试很有用。 |  |
| <input type="checkbox" unchecked id="switch_0381"> | `disable-component-update` | `kDisableComponentUpdate` | 禁用组件更新。 |  |
| <input type="checkbox" unchecked id="switch_0382"> | `disable-crashpad-for-testing` | `kDisableCrashpadForTesting` | 禁用crashpad初始化进行测试。crashpad二进制文件将不会运行，因此不会检测和符号化崩溃。 |  |
| <input type="checkbox" unchecked id="switch_0383"> | `disable-default-apps` | `kDisableDefaultApps` | 禁用首次运行时安装默认应用。这在自动测试期间使用。 |  |
| <input type="checkbox" unchecked id="switch_0384"> | `disable-domain-reliability` | `kDisableDomainReliability` | 禁用域可靠性监控。 |  |
| <input type="checkbox" unchecked id="switch_0385"> | `disable-print-preview` | `kDisablePrintPreview` | 禁用打印预览（用于测试，以及不喜欢我们的用户。:[） |  |
| <input type="checkbox" unchecked id="switch_0386"> | `disable-prompt-on-repost` | `kDisablePromptOnRepost` | 通常当用户尝试导航到POST结果页面时，我们会提示确认是否要这样做。此开关可用于禁用该检查。此开关在自动测试期间使用。 |  |
| <input type="checkbox" unchecked id="switch_0387"> | `disable-stack-profiler` | `kDisableStackProfiler` | 禁用堆栈分析器。堆栈分析可能会改变性能。当与默认禁用它的构建比较性能指标时，禁用堆栈分析是有益的。 |  |
| <input type="checkbox" unchecked id="switch_0388"> | `disable-zero-browsers-open-for-tests` | `kDisableZeroBrowsersOpenForTests` | 某些测试似乎要求当最后一个浏览器窗口关闭时应用程序关闭。因此，我们需要一个开关来强制ChromeOS Aura的这种行为，禁用"零窗口模式"。TODO(pkotwicz)：调查是否可以删除此错误。(http://crbug.com/119175) |  |
| <input type="checkbox" unchecked id="switch_0389"> | `disk-cache-size` | `kDiskCacheSize` | 强制磁盘缓存使用的最大磁盘空间，以字节为单位。 |  |
| <input type="checkbox" unchecked id="switch_0390"> | `do-not-de-elevate` | `kDoNotDeElevateOnLaunch` | 启动时不降低浏览器权限。在降权后使用以防止无限循环。 |  |
| <input type="checkbox" unchecked id="switch_0391"> | `dump-browser-histograms` | `kDumpBrowserHistograms` | 请求运行中的浏览器进程将其收集的直方图转储到给定文件。如果文件存在将被覆盖。 |  |
| <input type="checkbox" unchecked id="switch_0392"> | `enable-audio-debug-recordings-from-extension` | `kEnableAudioDebugRecordingsFromExtension` | 如果WebRTC日志记录私有API处于活动状态，启用音频调试录音。 |  |
| <input type="checkbox" unchecked id="switch_0393"> | `enable-bookmark-undo` | `kEnableBookmarkUndo` | 启用书签的多级撤销系统。 |  |
| <input type="checkbox" unchecked id="switch_0394"> | `enable-cloud-print-proxy` | `kEnableCloudPrintProxy` | 这仅在进程类型为"service"时适用。在服务进程中启用云打印代理组件。 |  |
| <input type="checkbox" unchecked id="switch_0395"> | `enable-domain-reliability` | `kEnableDomainReliability` | 启用域可靠性监控。 |  |
| <input type="checkbox" unchecked id="switch_0396"> | `enable-extension-activity-log-testing` | `kEnableExtensionActivityLogTesting` | 启用扩展活动日志测试。 |  |
| <input type="checkbox" unchecked id="switch_0397"> | `enable-extension-activity-logging` | `kEnableExtensionActivityLogging` | 启用扩展活动日志记录。 |  |
| <input type="checkbox" unchecked id="switch_0398"> | `enable-extension-actor-api` | `kExtensionExperimentalActor` | 允许实验性actor API的命令行标志名称。 |  |
| <input type="checkbox" unchecked id="switch_0399"> | `enable-extension-ai-data-collection` | `kExtensionAiDataCollection` | 允许AI数据收集扩展API的命令行标志名称。 |  |
| <input type="checkbox" unchecked id="switch_0400"> | `enable-hangout-services-extension-for-testing` | `kEnableHangoutServicesExtensionForTesting` | 强制启用HangoutServicesExtension。 |  |
| <input type="checkbox" unchecked id="switch_0401"> | `enable-net-benchmarking` | `kEnableNetBenchmarking` | 启用与网络相关的基准测试扩展。 |  |
| <input type="checkbox" unchecked id="switch_0402"> | `enable-potentially-annoying-security-features` | `kEnablePotentiallyAnnoyingSecurityFeatures` | 启用一些潜在令人烦恼的安全功能（严格混合内容模式、强大功能限制等）。 |  |
| <input type="checkbox" unchecked id="switch_0403"> | `enable-unsafe-extension-debugging` | `kEnableUnsafeExtensionDebugging` | 如果协议客户端通过--remote-debugging-pipe连接，则允许通过Chrome DevTools协议在运行时安装/卸载扩展。 |  |
| <input type="checkbox" unchecked id="switch_0404"> | `enforce` | `kExtensionContentVerificationEnforce` | 强制扩展内容验证。 |  |
| <input type="checkbox" unchecked id="switch_0405"> | `enforce_strict` | `kExtensionContentVerificationEnforceStrict` | 严格强制扩展内容验证。 |  |
| <input type="checkbox" unchecked id="switch_0406"> | `experimental-ai-stable-channel` | `kExperimentalAiStableChannel` | 允许在稳定频道中使用实验性AI扩展API。如果设置，无论频道如何，这都会禁用Chrome登录。 |  |
| <input type="checkbox" unchecked id="switch_0407"> | `extension-content-verification` | `kExtensionContentVerification` | 在各种模式之一中强制启用内容验证的命令行标志名称。 |  |
| <input type="checkbox" unchecked id="switch_0408"> | `extensions-install-verification` | `kExtensionsInstallVerification` | 如果原本不会启用扩展安装验证，则启用它。 |  |
| <input type="checkbox" unchecked id="switch_0409"> | `extensions-not-webstore` | `kExtensionsNotWebstore` | 指定一个逗号分隔的扩展ID列表，在进行安装验证时应强制将其视为非来自webstore。 |  |
| <input type="checkbox" unchecked id="switch_0410"> | `extensions-toolbar-zero-state-explore-extensions-by-category` | `kExtensionsToolbarZeroStateExploreExtensionsByCategory` | 零状态扩展工具栏推荐的此变体建议用户可以在Chrome Web Store中探索的扩展类别。（例如，查找优惠券，提高生产力） |  |
| <input type="checkbox" unchecked id="switch_0411"> | `extensions-toolbar-zero-state-single-web-store-link` | `kExtensionsToolbarZeroStateSingleWebStoreLink` | 零状态扩展工具栏推荐的此变体向用户提供Chrome Web Store主页的单个链接。 |  |
| <input type="checkbox" unchecked id="switch_0412"> | `extensions-toolbar-zero-state-variation` | `kExtensionsToolbarZeroStateVariation` | 指定要显示的零状态扩展工具栏推荐的变体。当安装了零扩展的用户点击Chrome工具栏中的扩展拼图块时，Chrome显示一个子菜单，建议用户探索Chrome Web Store。 |  |
| <input type="checkbox" unchecked id="switch_0413"> | `force-app-mode` | `kForceAppMode` | 强制应用程序模式。这会隐藏某些系统UI元素，如果应用尚未安装，则强制安装该应用。 |  |
| <input type="checkbox" unchecked id="switch_0414"> | `force-first-run` | `kForceFirstRun` | 无论是否实际是首次运行，浏览器启动时都显示首次运行体验（这会覆盖kNoFirstRun）。 |  |
| <input type="checkbox" unchecked id="switch_0415"> | `force-whats-new` | `kForceWhatsNew` | 如果当前里程碑尚未显示，则浏览器启动时显示"新功能"体验（这会覆盖kNoFirstRun，而不显示首次运行体验）。 |  |
| <input type="checkbox" unchecked id="switch_0416"> | `hide-crash-restore-bubble` | `kHideCrashRestoreBubble` | 在ChromeOS中，如果启用了ChromeOS完整恢复功能，当浏览器在系统启动阶段启动时不显示崩溃恢复气泡，因为会显示ChromeOS完整恢复通知供用户选择是否恢复。 |  |
| <input type="checkbox" unchecked id="switch_0417"> | `homepage` | `kHomePage` | 指定在新打开的标签页中显示哪个页面。我们需要这个用于测试目的，以便UI测试不依赖于http://google.com出现的内容。 |  |
| <input type="checkbox" unchecked id="switch_0418"> | `ignore-profile-directory-if-not-exists` | `kIgnoreProfileDirectoryIfNotExists` | 如果与kProfileDirectory一起提供，当配置文件目录不存在时不创建配置文件。 |  |
| <input type="checkbox" unchecked id="switch_0419"> | `init-isolate-as-foreground` | `kInitIsolateAsForeground` | 指定主线程Isolate应在前台模式下初始化。如果未指定，Isolate对于扩展进程将在后台模式下启动，否则在前台模式下启动。 |  |
| <input type="checkbox" unchecked id="switch_0420"> | `install-autogenerated-theme` | `kInstallAutogeneratedTheme` | 根据给定的RGB值安装自动生成的主题。格式为"r,g,b"，其中r、g、b是0到255的数值。 |  |
| <input type="checkbox" unchecked id="switch_0421"> | `install-chrome-app` | `kInstallChromeApp` | 使Chrome为给定应用启动安装流程。 |  |
| <input type="checkbox" unchecked id="switch_0422"> | `install-isolated-web-app-from-file` | `kInstallIsolatedWebAppFromFile` | 使Chrome将给定路径的未签名Web Bundle作为开发者模式隔离Web应用安装。 |  |
| <input type="checkbox" unchecked id="switch_0423"> | `install-isolated-web-app-from-url` | `kInstallIsolatedWebAppFromUrl` | 使Chrome安装内容托管在给定HTTP(S) URL的开发者模式隔离Web应用。 |  |
| <input type="checkbox" unchecked id="switch_0424"> | `instant-process` | `kInstantProcess` | 将渲染器标记为即时进程。 |  |
| <input type="checkbox" unchecked id="switch_0425"> | `keep-alive-for-test` | `kKeepAliveForTest` | 用于测试 - 在最后一个浏览器窗口关闭后保持浏览器活动。 |  |
| <input type="checkbox" unchecked id="switch_0426"> | `kiosk` | `kKioskMode` | 启用kiosk模式。请注意这不是Chrome OS kiosk模式。 |  |
| <input type="checkbox" unchecked id="switch_0427"> | `kiosk-printing` | `kKioskModePrinting` | 在打印预览中启用自动按下打印按钮。 |  |
| <input type="checkbox" unchecked id="switch_0428"> | `make-default-browser` | `kMakeDefaultBrowser` | 使Chrome成为默认浏览器。 |  |
| <input type="checkbox" unchecked id="switch_0429"> | `monitoring-destination-id` | `kMonitoringDestinationID` | 允许为连接监控GCM消息设置不同的目标ID。在针对非生产管理服务器运行时很有用。 |  |
| <input type="checkbox" unchecked id="switch_0430"> | `native-messaging-connect-extension` | `kNativeMessagingConnectExtension` | 请求在此开关指定ID的扩展与由kNativeMessagingConnectHost开关命名的本机消息传递主机之间建立本机消息传递连接。 |  |
| <input type="checkbox" unchecked id="switch_0431"> | `native-messaging-connect-host` | `kNativeMessagingConnectHost` | 请求在此开关命名的本机消息传递主机与由kNativeMessagingConnectExtension指定ID的扩展之间建立本机消息传递连接。 |  |
| <input type="checkbox" unchecked id="switch_0432"> | `native-messaging-connect-id` | `kNativeMessagingConnectId` | 如果在指定kNativeMessagingConnectHost和kNativeMessagingConnectExtension时设置，作为命令行参数反映给本机消息传递主机。 |  |
| <input type="checkbox" unchecked id="switch_0433"> | `new-window` | `kOpenInNewWindow` | 在新浏览器窗口中启动URL。 |  |
| <input type="checkbox" unchecked id="switch_0434"> | `no-default-browser-check` | `kNoDefaultBrowserCheck` | 禁用默认浏览器检查。对于UI/浏览器测试很有用，我们希望避免显示默认浏览器信息栏。 |  |
| <input type="checkbox" unchecked id="switch_0435"> | `no-experiments` | `kNoExperiments` | 禁用about:flags上设置的所有实验。不禁用about:flags本身。如果实验导致chrome在启动时崩溃，这很有用：可以用--no-experiments启动chrome，在about:flags禁用有问题的实验室，然后不再使用此开关重启chrome。 |  |
| <input type="checkbox" unchecked id="switch_0436"> | `no-first-run` | `kNoFirstRun` | 跳过首次运行任务以及不显示额外的对话框、提示或气泡。抑制对话框、提示和气泡很重要，因为此开关由自动化（包括性能基准测试）使用，其中只显示浏览器窗口很重要。这可能实际上不是首次运行或"新功能"页面。其效果可以通过添加kForceFirstRun（用于FRE）、kForceWhatsNew（用于新功能）和/或kIgnoreNoFirstRunForSearchEngineChoiceScreen（用于DSE选择屏幕）部分忽略。这不会删除首次运行标记，因此不会阻止下次启动chrome而不使用此标志时发生首次运行。它也不更新最后的"新功能"里程碑，所以不会阻止下次启动chrome而不使用此标志时发生"新功能"。 |  |
| <input type="checkbox" unchecked id="switch_0437"> | `no-pings` | `kNoPings` | 不发送超链接审核ping。 |  |
| <input type="checkbox" unchecked id="switch_0438"> | `no-proxy-server` | `kNoProxyServer` | 不使用代理服务器，始终建立直接连接。覆盖传递的任何其他代理服务器标志。 |  |
| <input type="checkbox" unchecked id="switch_0439"> | `no-service-autorun` | `kNoServiceAutorun` | 禁用服务进程将自身添加为自动运行进程。这不删除现有的自动运行注册，它只是阻止服务注册新的。 |  |
| <input type="checkbox" unchecked id="switch_0440"> | `no-startup-window` | `kNoStartupWindow` | 启动时不自动打开浏览器窗口（在启动Chrome以托管后台应用时使用）。 |  |
| <input type="checkbox" unchecked id="switch_0441"> | `on-the-fly-mhtml-hash-computation` | `kOnTheFlyMhtmlHashComputation` | 在保存MHTML文件时计算其哈希值。浏览器进程将序列化的MHTML内容写入文件，并在通过Mojo数据管道从渲染器流式传输回来时计算其哈希值。 |  |
| <input type="checkbox" unchecked id="switch_0442"> | `pack-extension` | `kPackExtension` | 将扩展从给定目录打包为.crx可安装文件。 |  |
| <input type="checkbox" unchecked id="switch_0443"> | `pack-extension-key` | `kPackExtensionKey` | 用于签署打包.crx的可选PEM私钥。 |  |
| <input type="checkbox" unchecked id="switch_0444"> | `password-change-url` | `kPasswordChangeUrl` | 此开关允许在提供的URL上测试密码更改功能。通过在具有匹配eTLD+1的任何URL上提交密码表单来提供密码更改。 |  |
| <input type="checkbox" unchecked id="switch_0445"> | `pre-crashpad-crash-test` | `kPreCrashpadCrashTest` | 使浏览器进程在启动的很早阶段崩溃，就在crashpad（或breakpad）初始化之前。 |  |
| <input type="checkbox" unchecked id="switch_0446"> | `prediction-service-mock-likelihood` | `kPredictionServiceMockLikelihood` | 用于模拟从Web权限预测服务接收的响应。用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0447"> | `preinstalled-web-apps-dir` | `kPreinstalledWebAppsDir` | Chrome查找描述默认/预安装Web应用的json文件的目录。这会覆盖加载预安装Web应用的任何默认目录。 |  |
| <input type="checkbox" unchecked id="switch_0448"> | `privet-ipv6-only` | `kPrivetIPv6Only` | 仅对privet HTTP使用IPv6。 |  |
| <input type="checkbox" unchecked id="switch_0449"> | `product-version` | `kProductVersion` | 输出产品版本信息并退出。用作检测Linux上已安装Chrome版本的内部API。 |  |
| <input type="checkbox" unchecked id="switch_0450"> | `profile-directory` | `kProfileDirectory` | 选择与第一个启动的浏览器关联的配置文件目录。 |  |
| <input type="checkbox" unchecked id="switch_0451"> | `profile-email` | `kProfileEmail` | 类似于kProfileDirectory，但通过电子邮件地址选择配置文件。如果在任何现有配置文件中找不到电子邮件，此开关无效。如果同时指定kProfileDirectory和kProfileEmail，kProfileDirectory优先。 |  |
| <input type="checkbox" unchecked id="switch_0452"> | `proxy-auto-detect` | `kProxyAutoDetect` | 强制代理自动检测。 |  |
| <input type="checkbox" unchecked id="switch_0453"> | `proxy-pac-url` | `kProxyPacUrl` | 使用给定URL处的pac脚本。 |  |
| <input type="checkbox" unchecked id="switch_0454"> | `remote-debugging-targets` | `kRemoteDebuggingTargets` | 提供用于发现DevTools远程调试目标的地址列表。格式为<host>:<port>,...,<host>:port。 |  |
| <input type="checkbox" unchecked id="switch_0455"> | `repair-all-valid-extensions` | `kRepairAllValidExtensions` | 指示如果所有损坏的扩展都被策略启用，则应修复它们。这主要在用户数据降级后使用。 |  |
| <input type="checkbox" unchecked id="switch_0456"> | `restart` | `kRestart` | 指示Chrome已重启（例如，标志更改后）。这用于在记录Launch.Mode2指标时忽略启动。 |  |
| <input type="checkbox" unchecked id="switch_0457"> | `restore-last-session` | `kRestoreLastSession` | 指示在启动时应恢复最后一个会话。这会覆盖首选项值。请注意，这不会在崩溃后强制自动会话恢复，以防止崩溃循环。此开关用于在OS X和Windows上实现对操作系统特定的"从上次停止的地方继续"功能的支持。 |  |
| <input type="checkbox" unchecked id="switch_0458"> | `same-tab` | `kSameTab` | 指示命令行中的URL应在活动标签页而不是新标签页中打开。如果给出多个URL作为参数，第一个将替换活动标签页。 |  |
| <input type="checkbox" unchecked id="switch_0459"> | `save-page-as-mhtml` | `kSavePageAsMHTML` | 默认启用将网页保存为MHTML（网页，单个），而不是保存为HTML与子资源目录（网页，完整）。请参阅http://crbug.com/40179885了解如何删除此开关。 |  |
| <input type="checkbox" unchecked id="switch_0460"> | `silent-debugger-extension-api` | `kSilentDebuggerExtensionAPI` | 当扩展使用chrome.debugger页面附加到页面时不显示信息栏。需要附加到扩展后台页面。 |  |
| <input type="checkbox" unchecked id="switch_0461"> | `silent-launch` | `kSilentLaunch` | 使Chrome启动时默认不打开任何窗口。如果希望将Chrome用作ash服务器，这很有用。 |  |
| <input type="checkbox" unchecked id="switch_0462"> | `simulate-browsing-data-lifetime` | `kSimulateBrowsingDataLifetime` | 将BrowsingDataLifetime策略设置为非常短的值（比通常可能的更短）以用于测试目的。 |  |
| <input type="checkbox" unchecked id="switch_0463"> | `simulate-critical-update` | `kSimulateCriticalUpdate` | 模拟有关键更新可用。 |  |
| <input type="checkbox" unchecked id="switch_0464"> | `simulate-elevated-recovery` | `kSimulateElevatedRecovery` | 模拟需要提升权限来恢复升级频道。 |  |
| <input type="checkbox" unchecked id="switch_0465"> | `simulate-idle-timeout` | `kSimulateIdleTimeout` | 将IdleTimeout策略设置为非常短的值（比通常可能的更短）以用于测试目的。 |  |
| <input type="checkbox" unchecked id="switch_0466"> | `simulate-outdated` | `kSimulateOutdated` | 模拟当前版本已过时。 |  |
| <input type="checkbox" unchecked id="switch_0467"> | `simulate-outdated-no-au` | `kSimulateOutdatedNoAU` | 模拟当前版本已过时且自动更新已关闭。 |  |
| <input type="checkbox" unchecked id="switch_0468"> | `simulate-upgrade` | `kSimulateUpgrade` | 模拟有更新可用。 |  |
| <input type="checkbox" unchecked id="switch_0469"> | `ssl-version-max` | `kSSLVersionMax` | 指定最大SSL/TLS版本（"tls1.2"或"tls1.3"）。 |  |
| <input type="checkbox" unchecked id="switch_0470"> | `ssl-version-min` | `kSSLVersionMin` | 指定最小SSL/TLS版本（"tls1.2"或"tls1.3"）。 |  |
| <input type="checkbox" unchecked id="switch_0471"> | `start-maximized` | `kStartMaximized` | 启动浏览器时最大化，无论之前的任何设置。 |  |
| <input type="checkbox" unchecked id="switch_0472"> | `start-stack-profiler` | `kStartStackProfiler` | 在子进程中启动堆栈采样分析器。 |  |
| <input type="checkbox" unchecked id="switch_0473"> | `storage-pressure-notification-interval` | `kStoragePressureNotificationInterval` | 用于存储压力通知节流的间隔（以分钟为单位）。对于测试可能使用非平凡磁盘空间量的应用程序的开发人员很有用。 |  |
| <input type="checkbox" unchecked id="switch_0474"> | `system-audio-capture-default_checked` | `kSystemAudioCaptureDefaultChecked` | 此标志将窗口或屏幕捕获期间共享系统音频的复选框默认设置为选中状态。它主要用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0475"> | `system-log-upload-frequency` | `kSystemLogUploadFrequency` | 系统日志上传的频率（以毫秒为单位）。应仅用于测试目的。 |  |
| <input type="checkbox" unchecked id="switch_0476"> | `tab-capture-audio-default-unchecked` | `kTabCaptureAudioDefaultUnchecked` | 此标志将标签页捕获期间共享音频的复选框默认设置为未选中状态。它主要用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0477"> | `test-memory-log-delay-in-minutes` | `kTestMemoryLogDelayInMinutes` | 内存日志的自定义延迟。这应该仅用于测试目的。 |  |
| <input type="checkbox" unchecked id="switch_0478"> | `test-name` | `kTestName` | 将当前运行的自动化测试名称传递给Chrome。 |  |
| <input type="checkbox" unchecked id="switch_0479"> | `tls1.2` | `kSSLVersionTLSv12` | 用于\|kSSLVersionMax\|和\|kSSLVersionMin\|开关的TLS 1.2模式。 |  |
| <input type="checkbox" unchecked id="switch_0480"> | `tls1.3` | `kSSLVersionTLSv13` | 用于\|kSSLVersionMax\|和\|kSSLVersionMin\|开关的TLS 1.3模式。 |  |
| <input type="checkbox" unchecked id="switch_0481"> | `trusted-download-sources` | `kTrustedDownloadSources` | 将下载源列表标识为可信，但仅在设置适当的组策略时。 |  |
| <input type="checkbox" unchecked id="switch_0482"> | `unlimited-storage` | `kUnlimitedStorage` | 为任何应用/源覆盖每个源的配额设置为无限存储。这应该仅用于测试目的。 |  |
| <input type="checkbox" unchecked id="switch_0483"> | `unsafely-disable-devtools-self-xss-warnings` | `kUnsafelyDisableDevToolsSelfXssWarnings` | 在粘贴到DevTools控制台时禁用有关自XSS攻击的警告。 |  |
| <input type="checkbox" unchecked id="switch_0484"> | `use-system-default-printer` | `kUseSystemDefaultPrinter` | 在打印预览中使用系统默认打印机作为初始选定的目标，而不是最近使用的目标。 |  |
| <input type="checkbox" unchecked id="switch_0485"> | `use-system-proxy-resolver` | `kUseSystemProxyResolver` | 使用WinHttp解析代理，而不是使用Chromium的正常代理解析逻辑。这仅在Windows中受支持。TODO(crbug.com/40111093)：仅在Chrome专门使用系统代理配置时使用WinHttp。 |  |
| <input type="checkbox" unchecked id="switch_0486"> | `validate-crx` | `kValidateCrx` | 检查.crx的有效性并打印结果。 |  |
| <input type="checkbox" unchecked id="switch_0487"> | `webrtc-event-log-proactive-pruning-delta` | `kWebRtcRemoteEventLogProactivePruningDelta` | 设置等待上传的远程绑定WebRTC事件日志之间主动修剪的延迟（以秒为单位）。所有正值都是合法的。所有负值都是非法的，将被忽略。如果设置为0，意思是"不进行主动修剪"。 |  |
| <input type="checkbox" unchecked id="switch_0488"> | `webrtc-event-log-upload-delay-ms` | `kWebRtcRemoteEventLogUploadDelayMs` | 仅当条件持续这么多毫秒时，WebRTC事件日志才会被上传。 |  |
| <input type="checkbox" unchecked id="switch_0489"> | `webrtc-event-log-upload-no-suppression` | `kWebRtcRemoteEventLogUploadNoSuppression` | 通常，远程绑定的WebRTC事件日志仅在没有对等连接活动时上传。使用此标志，上传永远不会被抑制。 |  |
| <input type="checkbox" unchecked id="switch_0490"> | `webrtc-ip-handling-policy` | `kWebRtcIPHandlingPolicy` | 覆盖WebRTC IP处理策略以模拟在首选项中指定WebRTC IP处理策略时的行为。 |  |
| <input type="checkbox" unchecked id="switch_0491"> | `win-jumplist-action` | `kWinJumplistAction` | 指定在Windows跳转列表中点击的类别选项，该选项导致浏览器启动。 |  |
| <input type="checkbox" unchecked id="switch_0492"> | `window-name` | `kWindowName` | 指定初始窗口用户标题：--window-name="My custom title" |  |
| <input type="checkbox" unchecked id="switch_0493"> | `window-position` | `kWindowPosition` | 指定初始窗口位置：--window-position=x,y |  |
| <input type="checkbox" unchecked id="switch_0494"> | `window-workspace` | `kWindowWorkspace` | 指定初始窗口工作区：--window-workspace=id |  |
| <input type="checkbox" unchecked id="switch_0495"> | `winhttp-proxy-resolver` | `kWinHttpProxyResolver` | 使用WinHTTP获取和评估PAC脚本。否则，默认是使用Chromium的网络堆栈获取，V8评估。 |  |

## Chrome Chrome Switches.cc, Content Content Switches.cc (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0496"> | `browser-test` | `kStartStackProfilerBrowserTest` | \|kStartStackProfiler\|开关的浏览器测试模式。将配置文件持续时间限制为显著少于测试超时时间。在ChromeOS上，强制堆栈采样分析器也在所有进程上运行。 |  |

## Chrome Chrome Switches.cc, Headless (10 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0497"> | `accept-lang` | `kAcceptLang` | 找不到您要查找的开关？请尝试查找：ash/constants/ash_switches.cc base/base_switches.cc 等。注释开关时，请使用与周围注释相同的语气。想象短语开头的"此开关..."，一切都会正常工作。指定要发送到服务器并通过navigator.language DOM属性公开给JavaScript的Accept-Language。language[-country]，其中language是ISO-639的2字母代码。 |  |
| <input type="checkbox" unchecked id="switch_0498"> | `auth-server-allowlist` | `kAuthServerAllowlist` | Negotiate Auth服务器的允许列表。 |  |
| <input type="checkbox" unchecked id="switch_0499"> | `disable-lazy-loading` | `kDisableLazyLoading` | 禁用图像和框架的延迟加载。 |  |
| <input type="checkbox" unchecked id="switch_0500"> | `disk-cache-dir` | `kDiskCacheDir` | 使用特定的磁盘缓存位置，而不是从UserDatadir派生的位置。 |  |
| <input type="checkbox" unchecked id="switch_0501"> | `explicitly-allowed-ports` | `kExplicitlyAllowedPorts` | 允许通过传递以逗号分隔的端口号列表来覆盖受限端口列表。 |  |
| <input type="checkbox" unchecked id="switch_0502"> | `incognito` | `kIncognito` | 使初始打开的浏览器处于无痕模式。其他浏览器可能处于或不处于无痕模式；请参见IncognitoModePrefs。 |  |
| <input type="checkbox" unchecked id="switch_0503"> | `proxy-bypass-list` | `kProxyBypassList` | 指定我们绕过代理设置并使用直接连接的主机列表。如果也指定了--proxy-auto-detect或--no-proxy-server，则忽略此选项。这是一个以逗号分隔的绕过规则列表。格式请参见："net/proxy_resolution/proxy_bypass_rules.h"。 |  |
| <input type="checkbox" unchecked id="switch_0504"> | `proxy-server` | `kProxyServer` | 使用指定的代理服务器，覆盖系统设置。此开关仅影响HTTP和HTTPS请求。 |  |
| <input type="checkbox" unchecked id="switch_0505"> | `version` | `kVersion` | 打印版本信息并退出。 |  |
| <input type="checkbox" unchecked id="switch_0506"> | `window-size` | `kWindowSize` | 设置初始窗口大小。以"800,600"格式提供字符串。这也定义了无头屏幕大小以代替--screen-info。 |  |

## Chrome Chrome Switches.cc, Headless, Shell (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0507"> | `user-data-dir` | `kUserDataDir` | 使Content Shell使用给定路径作为其数据目录。注意："user-data-dir"用于与Chromedriver的行为保持一致。请不要将其更改为其他值。注意：相同的值也在Java端的ContentShellBrowserTestActivity.java#getUserDataDirectoryCommandLineSwitch()中使用。 |  |

## Chrome Windows Services Service Program Switches.h (3 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0508"> | `log-file-handle` | `kLogFileHandle` | 传递服务应将其日志发送到的文件句柄值的开关。 |  |
| <input type="checkbox" unchecked id="switch_0509"> | `log-file-source` | `kLogFileSource` | 传递日志文件句柄值有效的进程PID的开关。 |  |
| <input type="checkbox" unchecked id="switch_0510"> | `unattended-test` | `kUnattendedTest` | 指示服务代表无人值守测试运行的开关（即在其环境块中设置了CHROME_HEADLESS的测试）。 |  |

## Chromecast (67 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0511"> | `accept-resource-provider` | `kAcceptResourceProvider` | 指示必须设置资源提供程序为cast接收器提供资源的标志。在提供资源之前，应用无法启动。此标志暗示--alsa-check-close-timeout=0。 |  |
| <input type="checkbox" unchecked id="switch_0512"> | `alsa-amp-device-name` | `kAlsaAmpDeviceName` | 应在其上打开放大器混音器的设备名称。如果未指定此标志，将默认为与kAlsaVolumeDeviceName相同的设备。 |  |
| <input type="checkbox" unchecked id="switch_0513"> | `alsa-amp-element-name` | `kAlsaAmpElementName` | 基于ALSA的媒体库应使用的简单混音器控制元素名称，用于在系统上切换省电模式。 |  |
| <input type="checkbox" unchecked id="switch_0514"> | `alsa-check-close-timeout` | `kAlsaCheckCloseTimeout` | 当没有更多混音器输入时，关闭PCM句柄前等待的时间（毫秒）。如果存在--accept-resource-provider，则假定为0。 |  |
| <input type="checkbox" unchecked id="switch_0515"> | `alsa-enable-upsampling` | `kAlsaEnableUpsampling` | 启用将采样率低于32kHz的音频重采样到48kHz的标志。内部音频产品应设置为true。 |  |
| <input type="checkbox" unchecked id="switch_0516"> | `alsa-fixed-output-sample-rate` | `kAlsaFixedOutputSampleRate` | 为alsa设备设置固定采样率的可选标志。已弃用：请改用--audio-output-sample-rate。 |  |
| <input type="checkbox" unchecked id="switch_0517"> | `alsa-mute-device-name` | `kAlsaMuteDeviceName` | 应在其上打开静音混音器的设备名称。如果未指定此标志，将默认为与kAlsaVolumeDeviceName相同的设备。 |  |
| <input type="checkbox" unchecked id="switch_0518"> | `alsa-mute-element-name` | `kAlsaMuteElementName` | 基于ALSA的媒体库应使用的简单混音器控制元素名称，用于静音系统。 |  |
| <input type="checkbox" unchecked id="switch_0519"> | `alsa-output-avail-min` | `kAlsaOutputAvailMin` | 调度传输的最小可用帧数。 |  |
| <input type="checkbox" unchecked id="switch_0520"> | `alsa-output-buffer-size` | `kAlsaOutputBufferSize` | ALSA输出缓冲区的帧大小。这直接设置输出设备的延迟。延迟可以通过将采样率乘以输出缓冲区大小来计算。 |  |
| <input type="checkbox" unchecked id="switch_0521"> | `alsa-output-period-size` | `kAlsaOutputPeriodSize` | ALSA输出周期的帧大小。ALSA输出设备的周期决定硬件中断之间经过多少帧。 |  |
| <input type="checkbox" unchecked id="switch_0522"> | `alsa-output-start-threshold` | `kAlsaOutputStartThreshold` | 输出开始前需要在输出缓冲区中有多少帧。 |  |
| <input type="checkbox" unchecked id="switch_0523"> | `alsa-volume-device-name` | `kAlsaVolumeDeviceName` | 应在其上打开音量控制混音器的设备名称。将使用与kAlsaOutputDevice相同的设备，如果未提供kAlsaOutputDevice则回退到"default"。 |  |
| <input type="checkbox" unchecked id="switch_0524"> | `alsa-volume-element-name` | `kAlsaVolumeElementName` | 基于ALSA的媒体库应使用的简单混音器控制元素名称，用于控制音量。 |  |
| <input type="checkbox" unchecked id="switch_0525"> | `audio-output-channels` | `kAudioOutputChannels` | 音频输出通道数。这将用于向ALSA发送具有特定通道数的音频缓冲区并生成回环音频。默认值为2。 |  |
| <input type="checkbox" unchecked id="switch_0526"> | `audio-output-sample-rate` | `kAudioOutputSampleRate` | 指定音频输出流的固定采样率。如果未指定此标志，StreamMixer将根据媒体流的采样率选择采样率。 |  |
| <input type="checkbox" unchecked id="switch_0527"> | `back-gesture-horizontal-threshold` | `kBackGestureHorizontalThreshold` | 从左滑手势开始算起被视为"返回"手势的像素数。 |  |
| <input type="checkbox" unchecked id="switch_0528"> | `bottom-gesture-start-height` | `kBottomSystemGestureStartHeight` | 从屏幕底部向上算起被视为底部滑动手势有效起点的像素数。如果设置，覆盖上述system-gesture-start-height标志的值和cast_system_gesture_handler.cc中的默认值。 |  |
| <input type="checkbox" unchecked id="switch_0529"> | `cast-app-background-color` | `kCastAppBackgroundColor` | Chromium尚未渲染任何内容时使用的背景色。 |  |
| <input type="checkbox" unchecked id="switch_0530"> | `cast-core-runtime-id` | `kCastCoreRuntimeId` | 指定Cast Core运行时ID，--cast-core-runtime-id=<runtime_id>。 |  |
| <input type="checkbox" unchecked id="switch_0531"> | `cast-core-service-endpoint` | `kCastCoreServiceEndpoint` | 指定Cast Core服务gRPC端点。 |  |
| <input type="checkbox" unchecked id="switch_0532"> | `cast-initial-screen-height` | `kCastInitialScreenHeight` | 初始屏幕高度。 |  |
| <input type="checkbox" unchecked id="switch_0533"> | `cast-initial-screen-width` | `kCastInitialScreenWidth` | 用于向GPU进程传递初始屏幕分辨率。这允许我们正确设置屏幕大小（因此在创建第一个窗口时无需调整大小）。 |  |
| <input type="checkbox" unchecked id="switch_0534"> | `cast-mojo-broker-path` | `kCastMojoBrokerPath` | 更改连接到Cast Mojo代理的Unix域套接字路径的命令行参数。 |  |
| <input type="checkbox" unchecked id="switch_0535"> | `connectivity-check-url` | `kConnectivityCheckUrl` | 用于网络连接检查的URL。默认为"https://clients3.google.com/generate_204"。 |  |
| <input type="checkbox" unchecked id="switch_0536"> | `crash-server-url` | `kCrashServerUrl` | 上传崩溃数据的服务器URL。生产设备默认为"https://clients2.google.com/cr/report"。非生产设备默认为"https://clients2.google.com/cr/staging_report"。 |  |
| <input type="checkbox" unchecked id="switch_0537"> | `daemon` | `kCrashUploaderDaemon` | 在crash_uploader中启用守护进程模式的开关。 |  |
| <input type="checkbox" unchecked id="switch_0538"> | `defer-feature-list` | `kDeferFeatureList` | 延迟在外部服务进程中初始化base::FeatureList，允许进程包含自己的非默认功能。 |  |
| <input type="checkbox" unchecked id="switch_0539"> | `desktop-window-1080p` | `kDesktopWindow1080p` | 存在时，桌面cast_shell将创建1080p窗口（前提是显示分辨率足够高）。否则，cast_shell默认为720p。 |  |
| <input type="checkbox" unchecked id="switch_0540"> | `disable-crashpad-forwarding` | `kDisableCrashpadForwarding` | 禁用Crashpad转发的开关。 |  |
| <input type="checkbox" unchecked id="switch_0541"> | `disable-mojo-renderer` | `kDisableMojoRenderer` | 不使用在媒体服务中远程托管的渲染器，而是回退到content_renderer内的默认渲染器。不更改媒体服务的行为。 |  |
| <input type="checkbox" unchecked id="switch_0542"> | `dumpstate-path` | `kDumpstateBinPath` | dumpstate二进制路径的开关。 |  |
| <input type="checkbox" unchecked id="switch_0543"> | `enable-grpc-over-tcpip` | `kEnableGrpcOverTcpIp` | 指定Cast Core应使用TCP/IP作为gRPC传输类型；否则使用UDS。 |  |
| <input type="checkbox" unchecked id="switch_0544"> | `enable-input` | `kEnableInput` | 启用窗口管理器的输入事件处理。 |  |
| <input type="checkbox" unchecked id="switch_0545"> | `enable-local-file-accesses` | `kEnableLocalFileAccesses` | 启用文件访问。大多数Cast设备不应启用此功能。 |  |
| <input type="checkbox" unchecked id="switch_0546"> | `enable-top-drag-gesture` | `kEnableTopDragGesture` | 是否启用"从顶部拖拽"手势的检测和分发。 |  |
| <input type="checkbox" unchecked id="switch_0547"> | `false` | `kSwitchValueFalse` | 指示命令行开关标志为false的值。 |  |
| <input type="checkbox" unchecked id="switch_0548"> | `force-media-resolution-height` | `kForceMediaResolutionHeight` | 存在时覆盖CanDisplayType API使用的屏幕分辨率，而不是使用从avsettings获得的值。 |  |
| <input type="checkbox" unchecked id="switch_0549"> | `force-media-resolution-width` | `kForceMediaResolutionWidth` | 强制媒体分辨率宽度。 |  |
| <input type="checkbox" unchecked id="switch_0550"> | `force-mojo-renderer` | `kForceMojoRenderer` | 强制使用mojo渲染器。换句话说，渲染器进程将运行mojo渲染器，CastRenderer将在浏览器进程中运行。这对于使用CastRenderer的设备是必需的。要使此标志生效，请注意您必须使用gn arg"enable_cast_renderer"设置为true构建cast web runtime，并且"renderer"必须包含在"mojo_media_services"列表中。此标志的优先级低于"disable-mojo-renderer"。 |  |
| <input type="checkbox" unchecked id="switch_0551"> | `force-update-remote-url` | `kForceUpdateRemoteUrl` | 强制更新UI远程URL的每个产品自定义，也用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0552"> | `graphics-buffer-count` | `kGraphicsBufferCount` | 图形缓冲区计数。 |  |
| <input type="checkbox" unchecked id="switch_0553"> | `in-process-broker` | `kInProcessBroker` | 在此进程内创建服务代理。只有一个进程应该托管服务代理。 |  |
| <input type="checkbox" unchecked id="switch_0554"> | `last-launched-app` | `kLastLaunchedApp` | 将应用ID信息传递给渲染器进程，用于日志记录。last-launched-app应该是刚启动并正在生成渲染器的应用。 |  |
| <input type="checkbox" unchecked id="switch_0555"> | `managed-mode` | `kManagedMode` | 是否处于接待模式。 |  |
| <input type="checkbox" unchecked id="switch_0556"> | `max-output-volume-dba1m` | `kMaxOutputVolumeDba1m` | 1米处语音内容的校准最大输出音量dBa（如果已知）。 |  |
| <input type="checkbox" unchecked id="switch_0557"> | `mem-pressure-system-reserved-kb` | `kMemPressureSystemReservedKb` | 一些平台通常有很少的"空闲"内存，但在缓冲区+缓存中有大量可用内存。对于这样的平台，将此数量配置为应视为不可用的缓冲区+缓存内存的部分。如果不使用此开关，将使用纯粹基于空闲内存的简单压力启发式算法。 |  |
| <input type="checkbox" unchecked id="switch_0558"> | `memory-pressure-critical-fraction` | `kCastMemoryPressureCriticalFraction` | Cast内存压力关键比例。 |  |
| <input type="checkbox" unchecked id="switch_0559"> | `memory-pressure-moderate-fraction` | `kCastMemoryPressureModerateFraction` | Cast内存压力中等比例。 |  |
| <input type="checkbox" unchecked id="switch_0560"> | `mixer-enable-dynamic-channel-count` | `kMixerEnableDynamicChannelCount` | 根据输入流在混音器中启用动态更改通道数。 |  |
| <input type="checkbox" unchecked id="switch_0561"> | `mixer-service-endpoint` | `kMixerServiceEndpoint` | 混音器服务监听的端点。这是UNIX域套接字的路径（默认为/tmp/mixer-service）。 |  |
| <input type="checkbox" unchecked id="switch_0562"> | `mixer-service-port` | `kMixerServicePort` | 在非Linux平台上混音器服务监听的TCP端口（默认12854）。 |  |
| <input type="checkbox" unchecked id="switch_0563"> | `mixer-source-audio-ready-threshold-ms` | `kMixerSourceAudioReadyThresholdMs` | 指定使用我们的混音器时音频输出的开始阈值帧。这主要用于将默认值覆盖为更大的值，适用于无法处理默认开始阈值而不遇到音频欠载的平台。 |  |
| <input type="checkbox" unchecked id="switch_0564"> | `mixer-source-input-queue-ms` | `kMixerSourceInputQueueMs` | 指定使用我们的混音器时音频输出的缓冲区大小。这主要用于将默认值覆盖为更大的值，适用于无法处理如此小的音频缓冲区而不遇到音频欠载的平台。 |  |
| <input type="checkbox" unchecked id="switch_0565"> | `netifs-to-ignore` | `kNetifsToIgnore` | 要忽略的网络接口列表。被忽略的接口将不用于网络连接。 |  |
| <input type="checkbox" unchecked id="switch_0566"> | `override-metrics-upload-url` | `kOverrideMetricsUploadUrl` | 覆盖发送指标日志的URL以供调试。 |  |
| <input type="checkbox" unchecked id="switch_0567"> | `previous-app` | `kPreviousApp` | 当last-launched-app启动时正在运行的应用。 |  |
| <input type="checkbox" unchecked id="switch_0568"> | `product-name` | `kCrashReportProductName` | 指定crash_uploader上传崩溃报告时使用的产品名称的开关。如果未指定则默认为"Eureka"。 |  |
| <input type="checkbox" unchecked id="switch_0569"> | `require-wlan` | `kRequireWlan` | 仅连接到WLAN接口。 |  |
| <input type="checkbox" unchecked id="switch_0570"> | `runtime-auth-token` | `kRuntimeAuthToken` | 安全地发送到运行时的认证令牌。 |  |
| <input type="checkbox" unchecked id="switch_0571"> | `runtime-service-path` | `kRuntimeServicePath` | 指定Cast Core运行时gRPC端点，--runtime-service-path=<endpoint>。 |  |
| <input type="checkbox" unchecked id="switch_0572"> | `sys-info-file-path` | `kSysInfoFilePath` | 系统信息文件路径。默认为空字符串，这意味着将使用虚拟信息。 |  |
| <input type="checkbox" unchecked id="switch_0573"> | `system-gesture-start-height` | `kSystemGestureStartHeight` | 从屏幕最顶部或底部开始计算被视为顶部或底部滑动手势有效起源的像素数。覆盖cast_system_gesture_handler.cc中的默认值。 |  |
| <input type="checkbox" unchecked id="switch_0574"> | `system-gesture-start-width` | `kSystemGestureStartWidth` | 从屏幕最左侧或右侧开始计算被视为左侧或右侧滑动手势有效起源的像素数。覆盖cast_system_gesture_handler.cc中的默认值。 |  |
| <input type="checkbox" unchecked id="switch_0575"> | `true` | `kSwitchValueTrue` | 指示命令行开关标志为true的值。 |  |
| <input type="checkbox" unchecked id="switch_0576"> | `use-cast-browser-pref-config` | `kUseCastBrowserPrefConfig` | 不与cast_service共享通用首选项配置文件，而是使用专用的浏览器首选项配置文件。当cast_browser在与cast_service不同的进程中运行时必须设置此项。 |  |
| <input type="checkbox" unchecked id="switch_0577"> | `vsync-interval` | `kVSyncInterval` | 覆盖GPU进程用于刷新显示的垂直同步间隔。 |  |

## Chromecast, Headless (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0578"> | `disable-crash-reporter` | `kDisableCrashReporter` | 在无头模式下禁用崩溃报告器。在官方构建中默认启用。 |  |

## Chromeos Constants Chromeos Switches.cc (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0579"> | `gemini-app-preinstall-activation-time-threshold` | `kGeminiAppPreinstallActivationTimeThreshold` | 用于为Gemini应用提供激活时间阈值的命令行开关名称。注意此开关仅用于测试目的。 |  |
| <input type="checkbox" unchecked id="switch_0580"> | `mahi-restrictions-override` | `kMahiRestrictionsOverride` | 在测试中用于覆盖mahi年龄和国家限制。 |  |

## Chromeos Services Machine Learning Cpp Ml Switches.cc (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0581"> | `ondevice_handwriting` | `kOndeviceHandwritingSwitch` | 用于确定是否以及如何支持设备上手写识别（例如通过rootfs或可下载内容）。 |  |

## Components Cast Streaming Browser Cast Streaming Switches.h (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0582"> | `cast-streaming-receiver-port` | `kCastStreamingReceiverPort` | 如果设置，允许在接收端为Cast流式传输会话使用特定的UDP端口。否则Cast流式传输接收器使用随机系统端口。 |  |

## Components Client Hints Switches.cc (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0583"> | `initialize-client-hints-storage` | `kInitializeClientHintsStorage` | 预加载客户端提示存储。接受一个JSON字典，每个键为一个源（RFC 6454第6.2节），每个值为客户端提示令牌的逗号分隔列表（RFC 8942第3.1节，client-hints-infrastructure第7.1节）。每个源/令牌列表条目将被解析并持久化到客户端提示存储中，就好像令牌列表是通过来自该源的导航的Accept-CH响应头传来的一样。初始化仅适用于非离线记录配置文件，意味着无痕或访客配置文件不会应用存储。 |  |

## Components Component Updater Component Updater Switches.cc (4 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0584"> | `campaigns-test-tag` | `kCampaignsTestTag` | 用于控制在测试队列中选择哪个服务活动文件版本的开关。例如：--campaigns-test-tag=dev1将选择标签匹配dev1的测试队列。 |  |
| <input type="checkbox" unchecked id="switch_0585"> | `component-updater` | `kComponentUpdater` | 用于故障排除组件更新器的逗号分隔选项。仅对浏览器进程有效。 |  |
| <input type="checkbox" unchecked id="switch_0586"> | `component-updater-trust-tokens-component-path` | `kComponentUpdaterTrustTokensComponentPath` | 信任令牌密钥承诺组件路径的可选测试覆盖。 |  |
| <input type="checkbox" unchecked id="switch_0587"> | `demo-app-test-tag` | `kDemoModeTestTag` | 用于控制在测试队列中选择哪个服务演示模式应用版本的开关。例如：--demo-app-test-tag=dev1将选择标签匹配dev1的测试队列。 |  |

## Components Dom Distiller Dom Distiller Switches.cc (10 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0588"> | `adaboost` | `kAdaBoost` |  |  |
| <input type="checkbox" unchecked id="switch_0589"> | `allarticles` | `kAllArticles` |  |  |
| <input type="checkbox" unchecked id="switch_0590"> | `alwaystrue` | `kAlwaysTrue` |  |  |
| <input type="checkbox" unchecked id="switch_0591"> | `discoverability` | `kReaderModeDiscoverabilityParamName` |  |  |
| <input type="checkbox" unchecked id="switch_0592"> | `enable-distillability-service` | `kEnableDistillabilityService` |  |  |
| <input type="checkbox" unchecked id="switch_0593"> | `enable-dom-distiller` | `kEnableDomDistiller` |  |  |
| <input type="checkbox" unchecked id="switch_0594"> | `offer-in-settings` | `kReaderModeOfferInSettings` |  |  |
| <input type="checkbox" unchecked id="switch_0595"> | `opengraph` | `kOGArticle` |  |  |
| <input type="checkbox" unchecked id="switch_0596"> | `reader-mode-feedback` | `kReaderModeFeedback` |  |  |
| <input type="checkbox" unchecked id="switch_0597"> | `reader-mode-heuristics` | `kReaderModeHeuristics` |  |  |

## Components Dom Distiller Dom Distiller Switches.cc, VR (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0598"> | `none` | `kWebXrHandAnonymizationStrategyNone` |  |  |

## Components Embedder Support Switches.cc (8 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0599"> | `disable-auto-reload` | `kDisableAutoReload` | 禁用错误页面的自动重新加载。 |  |
| <input type="checkbox" unchecked id="switch_0600"> | `disable-popup-blocking` | `kDisablePopupBlocking` | 禁用弹出窗口阻止。 |  |
| <input type="checkbox" unchecked id="switch_0601"> | `enable-auto-reload` | `kEnableAutoReload` | 启用错误页面的自动重新加载。 |  |
| <input type="checkbox" unchecked id="switch_0602"> | `origin-trial-disabled-features` | `kOriginTrialDisabledFeatures` | 包含应禁用原始试验实验的功能名称列表。名称应以"|"字符分隔。 |  |
| <input type="checkbox" unchecked id="switch_0603"> | `origin-trial-disabled-tokens` | `kOriginTrialDisabledTokens` | 包含应禁用原始试验实验的令牌签名列表。令牌应以"|"字符分隔。 |  |
| <input type="checkbox" unchecked id="switch_0604"> | `origin-trial-public-key` | `kOriginTrialPublicKey` | 将覆盖用于检查原始试验令牌的默认公钥的逗号分隔密钥列表。 |  |
| <input type="checkbox" unchecked id="switch_0605"> | `short-reporting-delay` | `kShortReportingDelay` | 将Reporting API延迟设置为不到一秒以允许更快的报告。 |  |
| <input type="checkbox" unchecked id="switch_0606"> | `use-mobile-user-agent` | `kUseMobileUserAgent` | 当Chromium应使用移动用户代理时设置。 |  |

## Components Embedder Support Switches.cc, Graphics (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0607"> | `headless` | `kHeadless` | 在无头模式下运行，即没有UI或显示服务器依赖。 |  |

## Components Embedder Support Switches.cc, Headless, iOS (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0608"> | `user-agent` | `kUserAgent` | 用于用自定义用户代理覆盖默认用户代理的字符串。 |  |

## Components Error Page Error Page Switches.cc (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0609"> | `disable-dinosaur-easter-egg` | `kDisableDinosaurEasterEgg` | 禁用离线间隔页面上的恐龙复活节彩蛋。 |  |
| <input type="checkbox" unchecked id="switch_0610"> | `enable-dinosaur-easter-egg-alt-images` | `kEnableDinosaurEasterEggAltGameImages` | 启用恐龙复活节彩蛋替代图像。 |  |

## Components Google Google Switches.cc (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0611"> | `google-base-url` | `kGoogleBaseURL` | 指定与Google通信时使用的替代URL。对测试很有用。 |  |
| <input type="checkbox" unchecked id="switch_0612"> | `ignore-google-port-numbers` | `kIgnoreGooglePortNumbers` | 设置时，这将忽略在google_util.h方法中传递的PortPermission并忽略端口号。这使得为使用这些方法（直接或间接）的功能运行测试变得更容易，使用EmbeddedTestServer，这更能代表生产环境。 |  |

## Components Heap Profiling In Process Switches.cc (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0613"> | `subproc-heap-profiling` | `kSubprocessHeapProfiling` | 为子进程强制开启堆分析。当子进程应该被分析时，浏览器会添加此参数。 |  |

## Components Media Router Providers Cast Certificate Switches.cc (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0614"> | `cast-developer-certificate-path` | `kCastDeveloperCertificatePath` | 当被构建标志启用时，传递此参数允许Cast身份验证工具在信任存储中使用自定义根开发者证书而不是根Google签名证书。 |  |
| <input type="checkbox" unchecked id="switch_0615"> | `cast-log-device-cert-chain` | `kCastLogDeviceCertChain` | 启用时，在VLOG级别3打印PEM编码的设备证书链。 |  |

## Components Network Session Configurator Network Switches.cc (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0616"> | `disable-http2-grease-settings` | `kDisableHttp2GreaseSettings` |  |  |
| <input type="checkbox" unchecked id="switch_0617"> | `http2-grease-settings` | `kEnableHttp2GreaseSettings` | kEnableHttp2GreaseSettings因历史原因不包含"enable"一词。 |  |

## Components Ntp Tiles Switches.cc (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0618"> | `enable-ntp-search-engine-country-detection` | `kEnableNTPSearchEngineCountryDetection` | 启用使用默认搜索引擎国家在NTP上显示特定国家的热门网站。 |  |

## Components Optimization Guide Optimization Guide Switches.cc (27 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0619"> | `disable-checking-optimization-guide-user-permissions` | `kDisableCheckingUserPermissionsForTesting` |  |  |
| <input type="checkbox" unchecked id="switch_0620"> | `disable-fetching-hints-at-navigation-start` | `kDisableFetchingHintsAtNavigationStartForTesting` |  |  |
| <input type="checkbox" unchecked id="switch_0621"> | `disable-model-download-verification` | `kDisableModelDownloadVerificationForTesting` |  |  |
| <input type="checkbox" unchecked id="switch_0622"> | `enable-model-quality-dogfood-logging` | `kEnableModelQualityDogfoodLogging` | 只要客户端是dogfood客户端，无论其他客户端设置如何都启用模型质量日志。 |  |
| <input type="checkbox" unchecked id="switch_0623"> | `enable-optimization-guide-debug-logs` | `kDebugLoggingEnabled` |  |  |
| <input type="checkbox" unchecked id="switch_0624"> | `model-quality-service-api-key` | `kModelQualityServiceAPIKey` | 覆盖用于发起远程请求的ModelQuality Service API密钥。 |  |
| <input type="checkbox" unchecked id="switch_0625"> | `model-quality-service-url` | `kModelQualityServiceURL` | 覆盖模型质量服务URL。 |  |
| <input type="checkbox" unchecked id="switch_0626"> | `ondevice-validation-request-override` | `kOnDeviceValidationRequestOverride` | 使设备上模型在启动后延迟运行验证。可以提供文本文件作为验证作业的输入，并可以提供输出文件路径来写入响应。 |  |
| <input type="checkbox" unchecked id="switch_0627"> | `ondevice-validation-write-to-file` | `kOnDeviceValidationWriteToFile` |  |  |
| <input type="checkbox" unchecked id="switch_0628"> | `optimization-guide-fetch-hints-override` | `kFetchHintsOverride` | 覆盖获取提示的调度和时间延迟，并在启动时使用提供的逗号分隔主机列表立即导致提示获取。 |  |
| <input type="checkbox" unchecked id="switch_0629"> | `optimization-guide-fetch-hints-override-timer` | `kFetchHintsOverrideTimer` | 覆盖提示获取调度和延迟，在启动时使用TopHostProvider立即导致提示获取。这用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0630"> | `optimization-guide-get-free-disk-space-with-user-visible-priority-task` | `kGetFreeDiskSpaceWithUserVisiblePriorityTask` |  |  |
| <input type="checkbox" unchecked id="switch_0631"> | `optimization-guide-google-api-key-configuration-check-override` | `kGoogleApiKeyConfigurationCheckOverride` | 启用覆盖权限的Google API密钥配置检查。 |  |
| <input type="checkbox" unchecked id="switch_0632"> | `optimization-guide-language-override` | `kOptimizationGuideLanguageOverride` | 允许向后端发送语言代码。 |  |
| <input type="checkbox" unchecked id="switch_0633"> | `optimization-guide-model-execution-enable-remote-debug-logging` | `kModelExecutionEnableRemoteDebugLogging` | 添加头信息以指示通过响应头从模型执行服务返回调试日志数据。 |  |
| <input type="checkbox" unchecked id="switch_0634"> | `optimization-guide-model-execution-validate` | `kModelExecutionValidate` | 触发服务器端AI模型执行的验证。用于集成测试。 |  |
| <input type="checkbox" unchecked id="switch_0635"> | `optimization-guide-model-override` | `kModelOverride` | 禁用模型的获取，并覆盖会话使用的文件路径和元数据，使用通过命令行传递的内容而不是已经存储的内容。我们期望字符串是模型覆盖的逗号分隔字符串，每个模型覆盖为：OPTIMIZATION_TARGET_STRING:file_path或OPTIMIZATION_TARGET_STRING:file_path:base64_encoded_any_proto_model_metadata。这可能只在桌面上工作，因为文件路径在Android上不太容易访问，但可能有用。 |  |
| <input type="checkbox" unchecked id="switch_0636"> | `optimization-guide-model-validate` | `kModelValidate` | 触发模型的验证。用于手动测试。 |  |
| <input type="checkbox" unchecked id="switch_0637"> | `optimization-guide-ondevice-model-adaptations-override` | `kOnDeviceModelAdaptationsOverride` | 覆盖设备上模型执行的设备上模型适应文件路径。 |  |
| <input type="checkbox" unchecked id="switch_0638"> | `optimization-guide-ondevice-model-execution-override` | `kOnDeviceModelExecutionOverride` | 覆盖设备上模型执行的设备上模型文件路径。 |  |
| <input type="checkbox" unchecked id="switch_0639"> | `optimization-guide-service-api-key` | `kOptimizationGuideServiceAPIKey` | 覆盖用于发起远程请求的优化指南服务API密钥。 |  |
| <input type="checkbox" unchecked id="switch_0640"> | `optimization-guide-service-get-hints-url` | `kOptimizationGuideServiceGetHintsURL` | 覆盖HintsFetcher将从中请求远程提示的优化指南服务URL。 |  |
| <input type="checkbox" unchecked id="switch_0641"> | `optimization-guide-service-get-models-url` | `kOptimizationGuideServiceGetModelsURL` | 覆盖PredictionModelFetcher将从中请求远程模型和主机功能的优化指南服务URL。 |  |
| <input type="checkbox" unchecked id="switch_0642"> | `optimization-guide-service-model-execution-url` | `kOptimizationGuideServiceModelExecutionURL` | 覆盖优化指南模型执行URL。 |  |
| <input type="checkbox" unchecked id="switch_0643"> | `optimization_guide_hints_override` | `kHintsProtoOverride` | 覆盖来自组件更新器的提示Protobuf。如果此开关的值无效，则使用常规提示处理。此开关的值应该是二进制Configuration消息的base64编码，可在optimization_guide的hints.proto中找到。为此开关提供有效值会导致Chrome启动时阻塞在提示解析上。 |  |
| <input type="checkbox" unchecked id="switch_0644"> | `purge-model-and-features-store` | `kPurgeModelAndFeaturesStore` | 在启动时清除包含预测模型和主机模型功能的存储，以确保使用新数据。 |  |
| <input type="checkbox" unchecked id="switch_0645"> | `purge-optimization-guide-store` | `kPurgeHintsStore` | 在启动时清除包含获取的和组件提示的存储，以确保使用新数据。 |  |

## Components Page Content Annotations Page Content Annotations Switches.cc (5 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0646"> | `enable-page-content-annotations-logging` | `kPageContentAnnotationsLoggingEnabled` |  |  |
| <input type="checkbox" unchecked id="switch_0647"> | `page-content-annotations-validation-batch-size` | `kPageContentAnnotationsValidationBatchSizeOverride` |  |  |
| <input type="checkbox" unchecked id="switch_0648"> | `page-content-annotations-validation-content-visibility` | `kPageContentAnnotationsValidationContentVisibility` | 启用特定注释类型在启动后延迟运行验证。可以给出逗号分隔的输入列表作为值，这些输入将用作验证作业的输入。 |  |
| <input type="checkbox" unchecked id="switch_0649"> | `page-content-annotations-validation-startup-delay-seconds` | `kPageContentAnnotationsValidationStartupDelaySeconds` |  |  |
| <input type="checkbox" unchecked id="switch_0650"> | `page-content-annotations-validation-write-to-file` | `kPageContentAnnotationsValidationWriteToFile` | 将页面内容注释验证的输出写入给定文件。 |  |

## Components Regional Capabilities Regional Capabilities Switches.h (3 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0651"> | `DEFAULT_EEA` | `kDefaultListCountryOverride` | kDefaultListCountryOverride和kEeaRegionCountryOverrideString是kSearchEngineChoiceCountry的特殊值。kDefaultListCountryOverride将覆盖搜索引擎列表以显示默认集合。kEeaListCountryOverride将覆盖搜索引擎列表以显示所有EEA引擎的列表。 |  |
| <input type="checkbox" unchecked id="switch_0652"> | `EEA_ALL` | `kEeaListCountryOverride` |  |  |
| <input type="checkbox" unchecked id="switch_0653"> | `search-engine-choice-country` | `kSearchEngineChoiceCountry` | 覆盖配置文件国家（其中包括用于搜索引擎选择区域检查等）。用于测试。期望2字母国家代码。 |  |

## Components Search Engines Search Engines Switches.cc (4 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0654"> | `disable-search-engine-choice-screen` | `kDisableSearchEngineChoiceScreen` |  |  |
| <input type="checkbox" unchecked id="switch_0655"> | `extra-search-query-params` | `kExtraSearchQueryParams` |  |  |
| <input type="checkbox" unchecked id="switch_0656"> | `force-search-engine-choice-screen` | `kForceSearchEngineChoiceScreen` |  |  |
| <input type="checkbox" unchecked id="switch_0657"> | `ignore-no-first-run-for-search-engine-choice-screen` | `kIgnoreNoFirstRunForSearchEngineChoiceScreen` |  |  |

## Components Search Engines Search Engines Switches.h (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0658"> | `NO_REPROMPT` | `kSearchEngineChoiceNoRepromptString` | 传递给switches::kSearchEngineChoiceTriggerRepromptParams的字符串，这样我们就不会用选择屏幕重新提示用户。 |  |

## Components Search Provider Logos Switches.cc (3 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0659"> | `google-doodle-url` | `kGoogleDoodleUrl` | 覆盖用于获取当前Google Doodle的URL。示例：https://www.google.com/async/ddljson 测试？试试：https://www.gstatic.com/chrome/ntp/doodle_test/ddljson_android0.json https://www.gstatic.com/chrome/ntp/doodle_test/ddljson_android1.json https://www.gstatic.com/chrome/ntp/doodle_test/ddljson_android2.json https://www.gstatic.com/chrome/ntp/doodle_test/ddljson_android3.json https://www.gstatic.com/chrome/ntp/doodle_test/ddljson_android4.json |  |
| <input type="checkbox" unchecked id="switch_0660"> | `search-provider-logo-url` | `kSearchProviderLogoURL` | 为默认搜索引擎的标识使用静态URL。示例：https://www.google.com/branding/logo.png |  |
| <input type="checkbox" unchecked id="switch_0661"> | `third-party-doodle-url` | `kThirdPartyDoodleURL` | 覆盖用于第三方搜索引擎的Doodle URL。测试？试试：https://www.gstatic.com/chrome/ntp/doodle_test/third_party_simple.json https://www.gstatic.com/chrome/ntp/doodle_test/third_party_animated.json |  |

## Components Ui Devtools Switches.cc (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0662"> | `enable-ui-devtools` | `kEnableUiDevTools` | 为UI（mus、ash等）启用DevTools服务器。值应该是服务器启动的端口。默认端口是9223。 |  |

## Components Webui Flags Flags Ui Switches.cc (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0663"> | `flag-switches-begin` | `kFlagSwitchesBegin` | 这两个标志被添加到about:flags添加到命令行的开关周围。这对于在about:version上查看哪些开关是由about:flags添加的很有用。它们没有任何效果。 |  |
| <input type="checkbox" unchecked id="switch_0664"> | `flag-switches-end` | `kFlagSwitchesEnd` |  |  |

## Compositor (7 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0665"> | `disable-vsync-for-tests` | `kDisableVsyncForTests` |  |  |
| <input type="checkbox" unchecked id="switch_0666"> | `enable-pixel-output-in-tests` | `kEnablePixelOutputInTests` | 强制测试在通常不会产生像素输出时产生像素输出。 |  |
| <input type="checkbox" unchecked id="switch_0667"> | `ui-disable-zero-copy` | `kUIDisableZeroCopy` |  |  |
| <input type="checkbox" unchecked id="switch_0668"> | `ui-enable-rgba-4444-textures` | `kUIEnableRGBA4444Textures` |  |  |
| <input type="checkbox" unchecked id="switch_0669"> | `ui-enable-zero-copy` | `kUIEnableZeroCopy` |  |  |
| <input type="checkbox" unchecked id="switch_0670"> | `ui-show-paint-rects` | `kUIShowPaintRects` |  |  |
| <input type="checkbox" unchecked id="switch_0671"> | `ui-slow-animations` | `kUISlowAnimations` |  |  |

## Content Content Switches.cc (197 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0672"> | `allow-command-line-plugins` | `kAllowCommandLinePlugins` | 允许在命令行中加载插件用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0673"> | `allow-file-access-from-files` | `kAllowFileAccessFromFiles` | 默认情况下，file:// URI无法读取其他file:// URI。这是为需要旧行为进行测试的开发者提供的覆盖选项。 |  |
| <input type="checkbox" unchecked id="switch_0674"> | `allow-insecure-localhost` | `kAllowInsecureLocalhost` | 启用对localhost上的TLS/SSL错误的忽略（没有间隔页，没有请求阻止）。 |  |
| <input type="checkbox" unchecked id="switch_0675"> | `allow-loopback-in-peer-connection` | `kAllowLoopbackInPeerConnection` | 允许在对等连接的网络列表中添加回环接口。 |  |
| <input type="checkbox" unchecked id="switch_0676"> | `arcore` | `kWebXrRuntimeArCore` | 以下是WebXr支持的运行时。 |  |
| <input type="checkbox" unchecked id="switch_0677"> | `as-browser` | `kLaunchAsBrowser` | 在浏览器进程中启动测试的标志。 |  |
| <input type="checkbox" unchecked id="switch_0678"> | `attribution-reporting-debug-mode` | `kAttributionReportingDebugMode` | 使Attribution Report API在没有延迟或噪声的情况下运行。 |  |
| <input type="checkbox" unchecked id="switch_0679"> | `auto-accept-camera-and-microphone-capture` | `kAutoAcceptCameraAndMicrophoneCapture` | 绕过提示用户授权捕获摄像头和麦克风的对话框。在视频会议Web应用程序的自动测试中很有用。这几乎与kUseFakeUIForMediaStream相同，除了这个标志不影响屏幕捕获。 |  |
| <input type="checkbox" unchecked id="switch_0680"> | `browser-startup-dialog` | `kBrowserStartupDialog` | 使浏览器进程在启动时显示对话框。 |  |
| <input type="checkbox" unchecked id="switch_0681"> | `browser-subprocess-path` | `kBrowserSubprocessPath` | 为渲染器和插件子进程运行的exe路径。 |  |
| <input type="checkbox" unchecked id="switch_0682"> | `browser-ui-tests-verify-pixels` | `kVerifyPixels` | 使测试尝试验证像素输出。 |  |
| <input type="checkbox" unchecked id="switch_0683"> | `canvas-2d-layers` | `kEnableCanvas2DLayers` | 启用正在进行中的canvas 2d API方法BeginLayer和EndLayer。 |  |
| <input type="checkbox" unchecked id="switch_0684"> | `cardboard` | `kWebXrRuntimeCardboard` |  |  |
| <input type="checkbox" unchecked id="switch_0685"> | `change-stack-guard-on-fork` | `kChangeStackGuardOnFork` | 在zygote分叉新进程后，更改栈金丝雀。这个开关很有用，这样不是所有分叉的进程都使用相同的金丝雀（一个秘密值），这可能容易受到信息泄露和暴力攻击的攻击。参见https://crbug.com/1206626。这要求在调用content::RunZygote()时栈上的所有函数都必须在没有栈金丝雀的情况下编译。有效值为"enable"或"disable"。 |  |
| <input type="checkbox" unchecked id="switch_0686"> | `crash-test` | `kBrowserCrashTest` | 使浏览器进程在启动时崩溃。 |  |
| <input type="checkbox" unchecked id="switch_0687"> | `disable` | `kChangeStackGuardOnForkDisabled` |  |  |
| <input type="checkbox" unchecked id="switch_0688"> | `disable-2d-canvas-clip-aa` | `kDisable2dCanvasClipAntialiasing` | 禁用2d画布剪切的抗锯齿 |  |
| <input type="checkbox" unchecked id="switch_0689"> | `disable-2d-canvas-image-chromium` | `kDisable2dCanvasImageChromium` | 禁用Canvas2D渲染到扫描缓冲区以支持覆盖。 |  |
| <input type="checkbox" unchecked id="switch_0690"> | `disable-3d-apis` | `kDisable3DAPIs` | 禁用客户端可见的3D API，特别是WebGL。这由策略控制，与其他启用/禁用开关分开，以避免意外回归对控制这些API访问的策略支持。 |  |
| <input type="checkbox" unchecked id="switch_0691"> | `disable-accelerated-2d-canvas` | `kDisableAccelerated2dCanvas` | 禁用GPU加速的2d画布。 |  |
| <input type="checkbox" unchecked id="switch_0692"> | `disable-accelerated-video-decode` | `kDisableAcceleratedVideoDecode` | 在可用的情况下禁用视频解码的硬件加速。警告：不要删除或重命名此标志，因为它在ChromeOS代码中用于实现DeviceHardwareVideoDecodingEnabled策略。 |  |
| <input type="checkbox" unchecked id="switch_0693"> | `disable-accelerated-video-encode` | `kDisableAcceleratedVideoEncode` | 在可用的情况下禁用视频编码的硬件加速。 |  |
| <input type="checkbox" unchecked id="switch_0694"> | `disable-back-forward-cache` | `kDisableBackForwardCache` | 禁用BackForwardCache功能。 |  |
| <input type="checkbox" unchecked id="switch_0695"> | `disable-background-timer-throttling` | `kDisableBackgroundTimerThrottling` | 禁用后台页面定时器任务的任务限制。 |  |
| <input type="checkbox" unchecked id="switch_0696"> | `disable-backgrounding-occluded-windows` | `kDisableBackgroundingOccludedWindowsForTesting` | 禁用被遮挡窗口的后台渲染。为测试而做，以避免不确定性行为。 |  |
| <input type="checkbox" unchecked id="switch_0697"> | `disable-backing-store-limit` | `kDisableBackingStoreLimit` | 禁用后备存储数量限制。可以防止拥有许多窗口/标签页和大量内存的用户出现闪烁。 |  |
| <input type="checkbox" unchecked id="switch_0698"> | `disable-blink-features` | `kDisableBlinkFeatures` | 禁用一个或多个Blink运行时启用的功能。使用来自runtime_enabled_features.json5的名称，用逗号分隔。在kEnableBlinkFeatures之后应用，也在更改这些功能的其他标志之后应用。 |  |
| <input type="checkbox" unchecked id="switch_0699"> | `disable-canvas-aa` | `kDisable2dCanvasAntialiasing` | 禁用2d画布的抗锯齿。 |  |
| <input type="checkbox" unchecked id="switch_0700"> | `disable-domain-blocking-for-3d-apis` | `kDisableDomainBlockingFor3DAPIs` | 在GPU重置后禁用3D API的按域阻止。这个开关仅用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0701"> | `disable-file-system` | `kDisableFileSystem` | 禁用FileSystem API。 |  |
| <input type="checkbox" unchecked id="switch_0702"> | `disable-gesture-requirement-for-presentation` | `kDisableGestureRequirementForPresentation` | 禁用演示的用户手势要求。 |  |
| <input type="checkbox" unchecked id="switch_0703"> | `disable-gpu` | `kDisableGpu` | 禁用GPU硬件加速。如果没有软件渲染器，则GPU进程不会启动。 |  |
| <input type="checkbox" unchecked id="switch_0704"> | `disable-gpu-compositing` | `kDisableGpuCompositing` | 防止合成器使用其GPU实现。 |  |
| <input type="checkbox" unchecked id="switch_0705"> | `disable-gpu-early-init` | `kDisableGpuEarlyInit` | 禁用GPU进程的主动早期初始化。 |  |
| <input type="checkbox" unchecked id="switch_0706"> | `disable-gpu-memory-buffer-compositor-resources` | `kDisableGpuMemoryBufferCompositorResources` | 不强制所有合成器资源都由GPU内存缓冲区支持。 |  |
| <input type="checkbox" unchecked id="switch_0707"> | `disable-gpu-memory-buffer-video-frames` | `kDisableGpuMemoryBufferVideoFrames` | 禁用GpuMemoryBuffer支持的VideoFrames。 |  |
| <input type="checkbox" unchecked id="switch_0708"> | `disable-gpu-process-crash-limit` | `kDisableGpuProcessCrashLimit` | 对于测试，禁用GPU进程可能重启次数的限制。 |  |
| <input type="checkbox" unchecked id="switch_0709"> | `disable-gpu-watchdog` | `kDisableGpuWatchdog` | 禁用当GPU进程停止响应消息时使其崩溃的线程。 |  |
| <input type="checkbox" unchecked id="switch_0710"> | `disable-histogram-customizer` | `kDisableHistogramCustomizer` | 禁用RenderThread的HistogramCustomizer。 |  |
| <input type="checkbox" unchecked id="switch_0711"> | `disable-ignore-duplicate-navs-for-testing` | `kDisableIgnoreDuplicateNavsForTesting` | 禁用IgnoreDuplicateNavs功能。这防止导航在测试中被无意忽略。 |  |
| <input type="checkbox" unchecked id="switch_0712"> | `disable-in-process-stack-traces` | `kDisableInProcessStackTraces` | 禁用进程内堆栈跟踪。 |  |
| <input type="checkbox" unchecked id="switch_0713"> | `disable-ipc-flooding-protection` | `kDisableIpcFloodingProtection` | 禁用IPC洪泛保护。它默认激活。一些JavaScript函数可以用来用IPC洪泛浏览器进程。这种保护限制了它们的使用率。 |  |
| <input type="checkbox" unchecked id="switch_0714"> | `disable-javascript-harmony-shipping` | `kDisableJavaScriptHarmonyShipping` | 禁用最新的发布ECMAScript 6功能。 |  |
| <input type="checkbox" unchecked id="switch_0715"> | `disable-kill-after-bad-ipc` | `kDisableKillAfterBadIPC` | 当子进程发送错误IPC消息时不杀死它。除了测试之外，从安全角度来看启用此开关是个坏主意。 |  |
| <input type="checkbox" unchecked id="switch_0716"> | `disable-lcd-text` | `kDisableLCDText` | 禁用LCD文本。 |  |
| <input type="checkbox" unchecked id="switch_0717"> | `disable-local-storage` | `kDisableLocalStorage` | 禁用LocalStorage。 |  |
| <input type="checkbox" unchecked id="switch_0718"> | `disable-logging` | `kDisableLogging` | 强制禁用日志记录。在调试版本中默认启用日志记录。 |  |
| <input type="checkbox" unchecked id="switch_0719"> | `disable-low-latency-dxva` | `kDisableLowLatencyDxva` | 禁用在创建DXVA解码器时使用CODECAPI_AVLowLatencyMode。 |  |
| <input type="checkbox" unchecked id="switch_0720"> | `disable-mojo-broker` | `kDisableMojoBroker` | 在Mojo初始化期间禁用浏览器中的Mojo代理功能。 |  |
| <input type="checkbox" unchecked id="switch_0721"> | `disable-new-content-rendering-timeout` | `kDisableNewContentRenderingTimeout` | 禁用在顶级框架导航后渲染器一段时间内没有提交新输出时清除渲染器的渲染输出。 |  |
| <input type="checkbox" unchecked id="switch_0722"> | `disable-notifications` | `kDisableNotifications` | 禁用Web通知和Push API。 |  |
| <input type="checkbox" unchecked id="switch_0723"> | `disable-nv12-dxgi-video` | `kDisableNv12DxgiVideo` | 禁用视频解码器绘制到NV12纹理而不是ARGB。 |  |
| <input type="checkbox" unchecked id="switch_0724"> | `disable-origin-trial-controlled-blink-features` | `kDisableOriginTrialControlledBlinkFeatures` | 禁用所有可以通过OriginTrials启用的RuntimeEnabledFeatures。 |  |
| <input type="checkbox" unchecked id="switch_0725"> | `disable-platform-accessibility-integration` | `kDisablePlatformAccessibilityIntegration` | 禁用通过与平台可访问性集成的交互激活浏览器和Web可访问性（即屏幕阅读器将无法与浏览器一起使用）。 |  |
| <input type="checkbox" unchecked id="switch_0726"> | `disable-presentation-api` | `kDisablePresentationAPI` | 禁用Presentation API。 |  |
| <input type="checkbox" unchecked id="switch_0727"> | `disable-pushstate-throttle` | `kDisablePushStateThrottle` | 禁用history.pushState/replaceState调用的限制。 |  |
| <input type="checkbox" unchecked id="switch_0728"> | `disable-reading-from-canvas` | `kDisableReadingFromCanvas` | 污染所有<canvas>元素，无论来源如何。 |  |
| <input type="checkbox" unchecked id="switch_0729"> | `disable-remote-fonts` | `kDisableRemoteFonts` | 禁用远程Web字体支持。无论是否指定此选项，SVG字体都应始终工作。 |  |
| <input type="checkbox" unchecked id="switch_0730"> | `disable-remote-playback-api` | `kDisableRemotePlaybackAPI` | 禁用RemotePlayback API。 |  |
| <input type="checkbox" unchecked id="switch_0731"> | `disable-renderer-backgrounding` | `kDisableRendererBackgrounding` | 设置时防止渲染器进程后台化。 |  |
| <input type="checkbox" unchecked id="switch_0732"> | `disable-resource-scheduler` | `kDisableResourceScheduler` | ResourceScheduler是否被禁用。注意这仅对需要实现自己的资源调度的C++ Headless嵌入器有用。 |  |
| <input type="checkbox" unchecked id="switch_0733"> | `disable-scroll-to-text-fragment` | `kDisableScrollToTextFragment` | 此开关禁用ScrollToTextFragment功能。 |  |
| <input type="checkbox" unchecked id="switch_0734"> | `disable-shared-workers` | `kDisableSharedWorkers` | 禁用共享工作者。 |  |
| <input type="checkbox" unchecked id="switch_0735"> | `disable-site-isolation-trials` | `kDisableSiteIsolation` | 禁用站点隔离。注意通过企业策略和/或命令行的选择加入（到站点per进程、隔离来源等）优先于kDisableSiteIsolation开关（即即使存在kDisableSiteIsolation开关，选择加入仍会生效）。注意由于历史原因，开关的名称误导性地提到了"trials"，但开关也禁用了自M67以来在桌面上发布的默认站点隔离。开关的名称为chrome://flags的向后兼容性而保留。 |  |
| <input type="checkbox" unchecked id="switch_0736"> | `disable-skia-runtime-opts` | `kDisableSkiaRuntimeOpts` | 不在Skia中使用运行时检测的高端CPU优化。这对于强制基准代码路径很有用，例如用于Web测试。 |  |
| <input type="checkbox" unchecked id="switch_0737"> | `disable-smooth-scrolling` | `kDisableSmoothScrolling` | 禁用平滑滚动用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0738"> | `disable-software-compositing-fallback` | `kDisableSoftwareCompositingFallback` | 对于测试，如果GPU进程已崩溃并达到GPU进程崩溃限制，则禁用回退到软件合成。 |  |
| <input type="checkbox" unchecked id="switch_0739"> | `disable-software-rasterizer` | `kDisableSoftwareRasterizer` | 禁用3D软件光栅化器的使用。 |  |
| <input type="checkbox" unchecked id="switch_0740"> | `disable-speech-api` | `kDisableSpeechAPI` | 禁用Web Speech API（语音识别和合成）。 |  |
| <input type="checkbox" unchecked id="switch_0741"> | `disable-speech-synthesis-api` | `kDisableSpeechSynthesisAPI` | 禁用Web Speech API的语音合成部分。 |  |
| <input type="checkbox" unchecked id="switch_0742"> | `disable-threaded-compositing` | `kDisableThreadedCompositing` | 禁用Web内容的多线程GPU合成。 |  |
| <input type="checkbox" unchecked id="switch_0743"> | `disable-v8-idle-tasks` | `kDisableV8IdleTasks` | 禁用V8空闲任务。 |  |
| <input type="checkbox" unchecked id="switch_0744"> | `disable-web-security` | `kDisableWebSecurity` | 不强制执行同源策略；仅用于网站测试。除非也存在--user-data-dir（由内容嵌入器定义），否则此开关无效。 |  |
| <input type="checkbox" unchecked id="switch_0745"> | `disable-webgl` | `kDisableWebGL` | 禁用所有版本的WebGL。 |  |
| <input type="checkbox" unchecked id="switch_0746"> | `disable-webgl-image-chromium` | `kDisableWebGLImageChromium` | 禁用WebGL渲染到扫描缓冲区以支持覆盖。 |  |
| <input type="checkbox" unchecked id="switch_0747"> | `disable-webgl2` | `kDisableWebGL2` | 禁用WebGL2。 |  |
| <input type="checkbox" unchecked id="switch_0748"> | `disable-webrtc-encryption` | `kDisableWebRtcEncryption` | 禁用WebRTC的RTP媒体加密。当Chrome嵌入Content时，它在稳定和测试版频道上忽略此开关。 |  |
| <input type="checkbox" unchecked id="switch_0749"> | `disable-yuv-image-decoding` | `kDisableYUVImageDecoding` | 对于支持的格式和情况，禁用YUV图像解码。除非启用GPU光栅化，否则无效。 |  |
| <input type="checkbox" unchecked id="switch_0750"> | `disable-zero-copy-dxgi-video` | `kDisableZeroCopyDxgiVideo` | 禁用视频解码器直接绘制到纹理。 |  |
| <input type="checkbox" unchecked id="switch_0751"> | `disallow-v8-feature-flag-overrides` | `kDisallowV8FeatureFlagOverrides` | 不允许覆盖v8功能标志。 |  |
| <input type="checkbox" unchecked id="switch_0752"> | `dom-automation` | `kDomAutomationController` | 指定是否需要在渲染器中绑定|DOMAutomationController|。这种绑定基于每帧进行，因此可能成为性能瓶颈。只有在自动化基于DOM的测试时才应启用它。 |  |
| <input type="checkbox" unchecked id="switch_0753"> | `enable` | `kChangeStackGuardOnForkEnabled` |  |  |
| <input type="checkbox" unchecked id="switch_0754"> | `enable-aggressive-domstorage-flushing` | `kEnableAggressiveDOMStorageFlushing` | 启用DOM存储的积极刷新以最小化数据丢失。 |  |
| <input type="checkbox" unchecked id="switch_0755"> | `enable-automation` | `kEnableAutomation` | 启用浏览器由自动化控制的指示。 |  |
| <input type="checkbox" unchecked id="switch_0756"> | `enable-blink-features` | `kEnableBlinkFeatures` | 启用一个或多个Blink运行时启用的功能。使用来自runtime_enabled_features.json5的名称，用逗号分隔。在kDisableBlinkFeatures之前应用，在更改这些功能的其他标志之后应用。 |  |
| <input type="checkbox" unchecked id="switch_0757"> | `enable-blink-test-features` | `kEnableBlinkTestFeatures` | 启用状态为"test"或状态为"experimental"的blink运行时启用功能，这些功能在运行Web测试时启用。 |  |
| <input type="checkbox" unchecked id="switch_0758"> | `enable-caret-browsing` | `kEnableCaretBrowsing` | 启用原生插入符浏览，其中可移动光标放在网页上，允许用户仅使用键盘选择和浏览非可编辑文本。参见https://crbug.com/977390获取i2i链接。 |  |
| <input type="checkbox" unchecked id="switch_0759"> | `enable-experimental-cookie-features` | `kEnableExperimentalCookieFeatures` | 将一组实验性/新添加的cookie相关功能一起打开的标志，作为例如测试的便利，以避免必须单独设置多个开关，这可能容易出错（更不用说繁琐）。没有相应的开关来禁用所有这些功能，因为这是不鼓励的，为了测试目的，您需要单独关闭它们以识别有问题的功能。目前这会打开：net::features::kSameSiteDefaultChecksMethodRigorously net::features::kCookieSameSiteConsidersRedirectChain net::features::kEnablePortBoundCookies net::features::kEnableSchemeBoundCookies |  |
| <input type="checkbox" unchecked id="switch_0760"> | `enable-experimental-web-platform-features` | `kEnableExperimentalWebPlatformFeatures` | 启用正在开发中的Web平台功能。 |  |
| <input type="checkbox" unchecked id="switch_0761"> | `enable-experimental-webassembly-features` | `kEnableExperimentalWebAssemblyFeatures` | 启用实验性WebAssembly功能。 |  |
| <input type="checkbox" unchecked id="switch_0762"> | `enable-gpu-memory-buffer-video-frames` | `kEnableGpuMemoryBufferVideoFrames` | 启用GpuMemoryBuffer支持的VideoFrames。 |  |
| <input type="checkbox" unchecked id="switch_0763"> | `enable-isolated-web-apps-in-renderer` | `kEnableIsolatedWebAppsInRenderer` | 在渲染器进程中启用隔离Web应用程序（IWA）。有两种启用IWA的方法：通过功能标志和通过企业策略。如果通过上述任何方式启用了IWA，则此标志将传递给渲染器进程。此标志不应从命令行使用。要从命令行启用IWA，应使用kIsolatedWebApps功能标志。 |  |
| <input type="checkbox" unchecked id="switch_0764"> | `enable-lcd-text` | `kEnableLCDText` | 启用LCD文本。 |  |
| <input type="checkbox" unchecked id="switch_0765"> | `enable-logging` | `kEnableLogging` | 强制启用日志记录。在发布版本中默认禁用日志记录。 |  |
| <input type="checkbox" unchecked id="switch_0766"> | `enable-network-information-downlink-max` | `kEnableNetworkInformationDownlinkMax` | 启用NetInfo API的type、downlinkMax属性。同时，当连接类型发生变化时，启用触发NetInfo API的change属性。 |  |
| <input type="checkbox" unchecked id="switch_0767"> | `enable-plugin-placeholder-testing` | `kEnablePluginPlaceholderTesting` | 启用插件占位符的测试功能。仅供内部使用。 |  |
| <input type="checkbox" unchecked id="switch_0768"> | `enable-precise-memory-info` | `kEnablePreciseMemoryInfo` | 使返回给window.performance.memory的值在共享工作者中更精细和更新。如果没有此标志，内存信息仍然可用，但会被分桶并更新频率较低。此标志也适用于工作者。 |  |
| <input type="checkbox" unchecked id="switch_0769"> | `enable-privacy-sandbox-ads-apis` | `kEnablePrivacySandboxAdsApis` | 启用隐私沙盒API：Attribution Reporting、Fledge、Topics、Fenced Frames、Shared Storage、Private Aggregation及其相关功能。 |  |
| <input type="checkbox" unchecked id="switch_0770"> | `enable-service-binary-launcher` | `kEnableServiceBinaryLauncher` | 如果为true，则使用ServiceProcessLauncher启动服务。这允许加载服务二进制文件而不是使用实用程序进程。这仅对测试有用。 |  |
| <input type="checkbox" unchecked id="switch_0771"> | `enable-skia-benchmarking` | `kEnableSkiaBenchmarking` | 启用Skia基准测试扩展。 |  |
| <input type="checkbox" unchecked id="switch_0772"> | `enable-smooth-scrolling` | `kEnableSmoothScrolling` | 在支持的平台上启用平滑滚动动画。 |  |
| <input type="checkbox" unchecked id="switch_0773"> | `enable-spatial-navigation` | `kEnableSpatialNavigation` | 启用空间导航 |  |
| <input type="checkbox" unchecked id="switch_0774"> | `enable-stats-collection-bindings` | `kStatsCollectionController` | 指定是否需要在渲染器中绑定|StatsCollectionController|。这种绑定基于每帧进行，因此可能成为性能瓶颈。只有在运行需要访问提供的统计信息的测试时才应启用它。 |  |
| <input type="checkbox" unchecked id="switch_0775"> | `enable-strict-mixed-content-checking` | `kEnableStrictMixedContentChecking` | 阻止来自安全上下文的所有不安全请求，并阻止用户覆盖该决定。 |  |
| <input type="checkbox" unchecked id="switch_0776"> | `enable-strict-powerful-feature-restrictions` | `kEnableStrictPowerfulFeatureRestrictions` | 阻止一些强大功能（例如设备方向）的不安全使用，这些功能我们尚未为整个Web弃用。 |  |
| <input type="checkbox" unchecked id="switch_0777"> | `enable-tracing-fraction` | `kEnableTracingFraction` | 当与范围(0,1]中的值一起指定时，将为运行的（大约）该百分比的测试启用--enable-tracing。这以稳定的方式完成，使得每次运行都选择相同的测试，并假设测试在可能值的范围内均匀散列。该标志将为这些测试启用所有跟踪类别，而对其余的不启用。此标志可以与其他跟踪开关（如--enable-tracing-format）一起使用，但任何其他将启用跟踪的开关将为所有测试打开跟踪。 |  |
| <input type="checkbox" unchecked id="switch_0778"> | `enable-usermedia-screen-capturing` | `kEnableUserMediaScreenCapturing` | 为MediaStream API启用屏幕捕获支持。 |  |
| <input type="checkbox" unchecked id="switch_0779"> | `enable-viewport` | `kEnableViewport` | 启用@viewport CSS规则的使用，允许页面控制其自身布局的方面。这也会打开触摸屏捏合手势。 |  |
| <input type="checkbox" unchecked id="switch_0780"> | `enable-vtune-support` | `kEnableVtune` | 启用Vtune分析器支持。 |  |
| <input type="checkbox" unchecked id="switch_0781"> | `enable-webgl-developer-extensions` | `kEnableWebGLDeveloperExtensions` | 启用通常不向Web平台公开的WebGL开发者扩展。 |  |
| <input type="checkbox" unchecked id="switch_0782"> | `enable-webgl-draft-extensions` | `kEnableWebGLDraftExtensions` | 启用尚未被社区批准的WebGL扩展。 |  |
| <input type="checkbox" unchecked id="switch_0783"> | `enable-webgl-image-chromium` | `kEnableWebGLImageChromium` | 启用WebGL渲染到扫描缓冲区以支持覆盖。 |  |
| <input type="checkbox" unchecked id="switch_0784"> | `file-url-path-alias` | `kFileUrlPathAlias` | 定义一个别名根目录，在文件URL中用替换字符串替换。格式为"/alias=/replacement"，这会将file:///alias/some/path.html转换为file:///replacement/some/path.html。 |  |
| <input type="checkbox" unchecked id="switch_0785"> | `force-presentation-receiver-for-testing` | `kForcePresentationReceiverForTesting` | 强制将页面加载为演示接收器。对于测试演示接收器特定行为很有用。规范：https://www.w3.org/TR/presentation-api/#interface-presentationreceiver |  |
| <input type="checkbox" unchecked id="switch_0786"> | `force-webrtc-ip-handling-policy` | `kForceWebRtcIPHandlingPolicy` | 覆盖WebRTC IP处理策略以模拟在首选项中指定WebRTC IP处理策略时的行为。 |  |
| <input type="checkbox" unchecked id="switch_0787"> | `force-webxr-runtime` | `kWebXrForceRuntime` | 强制启用并选择指定的webxr运行时。注意这提供了启用运行时的替代方法，并且还将功能性地禁用所有其他运行时。 |  |
| <input type="checkbox" unchecked id="switch_0788"> | `gpu-launcher` | `kGpuLauncher` | 启动GPU进程的额外命令行选项（通常用于调试）。像renderer-cmd-prefix一样使用。 |  |
| <input type="checkbox" unchecked id="switch_0789"> | `gpu-sandbox-start-early` | `kGpuSandboxStartEarly` | 在创建GL上下文之前启动GPU沙盒。 |  |
| <input type="checkbox" unchecked id="switch_0790"> | `gpu-startup-dialog` | `kGpuStartupDialog` | 使GPU进程在启动时显示对话框。 |  |
| <input type="checkbox" unchecked id="switch_0791"> | `hide-scrollbars` | `kHideScrollbars` | 阻止为Web内容创建滚动条。对于拍摄一致的屏幕截图很有用。 |  |
| <input type="checkbox" unchecked id="switch_0792"> | `in-process-gpu` | `kInProcessGPU` | 在浏览器进程中作为线程运行GPU进程。 |  |
| <input type="checkbox" unchecked id="switch_0793"> | `ipc-connection-timeout` | `kIPCConnectionTimeout` | 覆盖子进程在杀死自己之前等待来自浏览器的连接的超时时间（以秒为单位）。 |  |
| <input type="checkbox" unchecked id="switch_0794"> | `isolate-origins` | `kIsolateOrigins` | 为一组源要求专用进程，指定为逗号分隔列表。例如：--isolate-origins=https://www.foo.com,https://www.bar.com |  |
| <input type="checkbox" unchecked id="switch_0795"> | `isolation-by-default` | `kIsolationByDefault` | 启用Web面向的行为，这将在相对不远的将来的某个时点默认启用源隔离。https://crbug.com/1140371 |  |
| <input type="checkbox" unchecked id="switch_0796"> | `javascript-harmony` | `kJavaScriptHarmony` | 启用实验性Harmony（ECMAScript 6）功能。 |  |
| <input type="checkbox" unchecked id="switch_0797"> | `launch-time-ticks` | `kRendererProcessLaunchTimeTicks` | 浏览器启动渲染器进程的时间（以TimeTicks为单位）。 |  |
| <input type="checkbox" unchecked id="switch_0798"> | `log-file` | `kLogFile` | 覆盖用于通用日志记录的默认文件名（不影响记录哪些事件）。 |  |
| <input type="checkbox" unchecked id="switch_0799"> | `log-gpu-control-list-decisions` | `kLogGpuControlListDecisions` | 在强制执行阻止列表规则时记录GPU控制列表决策。 |  |
| <input type="checkbox" unchecked id="switch_0800"> | `log-level` | `kLoggingLevel` | 设置最小日志级别。有效值从0到3：INFO = 0，WARNING = 1，LOG_ERROR = 2，LOG_FATAL = 3。 |  |
| <input type="checkbox" unchecked id="switch_0801"> | `log-missing-unload-ack` | `kLogMissingUnloadACK` | 每当渲染框架的卸载超时被超过时记录错误。 |  |
| <input type="checkbox" unchecked id="switch_0802"> | `max-active-webgl-contexts` | `kMaxActiveWebGLContexts` | 允许用户覆盖每个渲染器进程的最大活动WebGL上下文数。 |  |
| <input type="checkbox" unchecked id="switch_0803"> | `max-decoded-image-size-mb` | `kMaxDecodedImageSizeMb` | 设置最大解码图像大小限制。 |  |
| <input type="checkbox" unchecked id="switch_0804"> | `max-gum-fps` | `kWebRtcMaxCaptureFramerate` | 覆盖在调用getUserMedia时可以指定的最大帧率。此标志需要一个值。示例：--max-gum-fps=17.5 |  |
| <input type="checkbox" unchecked id="switch_0805"> | `max-web-media-player-count` | `kMaxWebMediaPlayerCount` | 设置每个框架允许的WebMediaPlayers的最大数量。 |  |
| <input type="checkbox" unchecked id="switch_0806"> | `message-loop-type-ui` | `kMessageLoopTypeUi` | 指示实用程序进程应使用UI类型的消息循环运行。 |  |
| <input type="checkbox" unchecked id="switch_0807"> | `mock-cert-verifier-default-result-for-testing` | `kMockCertVerifierDefaultResultForTesting` | 设置MockCertVerifier的默认结果。这仅在测试代码中有效。 |  |
| <input type="checkbox" unchecked id="switch_0808"> | `mojo-local-storage` | `kMojoLocalStorage` | 使用基于Mojo的LocalStorage实现。 |  |
| <input type="checkbox" unchecked id="switch_0809"> | `no-unsandboxed-zygote` | `kNoUnsandboxedZygote` | 禁用未沙盒化的zygote。注意：此标志不应在大多数平台上使用。引入它是因为某些平台（例如Cast）内存非常有限，并且在浏览器进程运行时二进制文件不会更新。 |  |
| <input type="checkbox" unchecked id="switch_0810"> | `no-xr-runtime` | `kWebXrRuntimeNone` | 告诉WebXr假设它不支持任何运行时。 |  |
| <input type="checkbox" unchecked id="switch_0811"> | `no-zygote` | `kNoZygote` | 禁用使用zygote进程来分叉子进程。相反，子进程将被直接分叉和执行。注意--no-sandbox也应该与此标志一起使用，因为沙盒需要zygote才能工作。 |  |
| <input type="checkbox" unchecked id="switch_0812"> | `openxr` | `kWebXrRuntimeOpenXr` |  |  |
| <input type="checkbox" unchecked id="switch_0813"> | `orientation-sensors` | `kWebXrRuntimeOrientationSensors` |  |  |
| <input type="checkbox" unchecked id="switch_0814"> | `override-language-detection` | `kOverrideLanguageDetection` | 覆盖基于页面内容确定的语言检测结果。 |  |
| <input type="checkbox" unchecked id="switch_0815"> | `pdf-renderer` | `kPdfRenderer` | 运行非PPAPI PDF插件的渲染器进程。 |  |
| <input type="checkbox" unchecked id="switch_0816"> | `private-aggregation-developer-mode` | `kPrivateAggregationDeveloperMode` | 使私有聚合API在没有报告延迟的情况下运行。 |  |
| <input type="checkbox" unchecked id="switch_0817"> | `process-per-site` | `kProcessPerSite` | 为所有域启用"每站点进程"进程模型。此模式整合同站点页面，使它们共享单个进程。更多详细信息：- https://www.chromium.org/developers/design-documents/process-models - site_instance.h中的类注释，列出了支持的进程模型。重要：这不要与--site-per-process混淆（后者是关于隔离，而不是整合）。您可能想要另一个。 |  |
| <input type="checkbox" unchecked id="switch_0818"> | `process-per-tab` | `kProcessPerTab` | 在其自己的渲染器进程中运行每组脚本连接的标签（即BrowsingInstance）。我们默认为每个站点实例（即来自具有脚本连接的同一注册域的页面组）使用渲染器进程。TODO(creis)：此标志目前是无操作的。我们应该重构它以避免跨站点导航的"不必要"进程交换，但在安全需要时仍进行交换（例如，隔离源）。 |  |
| <input type="checkbox" unchecked id="switch_0819"> | `protected-audiences-consented-debug-token` | `kProtectedAudiencesConsentedDebugToken` | 使受保护受众竞价和拍卖API向受信任的拍卖服务器提供提供的调试密钥。这告诉服务器可以记录关于此用户拍卖的信息以帮助调试。 |  |
| <input type="checkbox" unchecked id="switch_0820"> | `pull-to-refresh` | `kPullToRefresh` | 启用或禁用响应垂直过度滚动的下拉刷新手势。将值设置为'0'以禁用功能，设置为'1'以同时为触摸板和触摸屏启用，设置为'2'以仅为触摸屏启用。默认为禁用。 |  |
| <input type="checkbox" unchecked id="switch_0821"> | `reduce-accept-language` | `kReduceAcceptLanguage` | 减少HTTP头和JS navigator.languages的accept-language，只保留最偏好的语言：https://github.com/Tanych/accept-language。 |  |
| <input type="checkbox" unchecked id="switch_0822"> | `reduce-accept-language-http` | `kReduceAcceptLanguageHTTP` | 减少HTTP头的accept-language，只在请求头中发送最偏好的语言：https://github.com/Tanych/accept-language。 |  |
| <input type="checkbox" unchecked id="switch_0823"> | `reduce-user-agent-minor-version` | `kReduceUserAgentMinorVersion` | 减少User-Agent字符串中的次版本号。此标志实现了用户代理减少的第4阶段：https://blog.chromium.org/2021/09/user-agent-reduction-origin-trial-and-dates.html。 |  |
| <input type="checkbox" unchecked id="switch_0824"> | `reduce-user-agent-platform-oscpu` | `kReduceUserAgentPlatformOsCpu` | 减少桌面User-Agent字符串中的平台和oscpu。此标志实现了用户代理减少的第5阶段：https://blog.chromium.org/2021/09/user-agent-reduction-origin-trial-and-dates.html。 |  |
| <input type="checkbox" unchecked id="switch_0825"> | `remote-allow-origins` | `kRemoteAllowOrigins` | 仅启用来自指定源的Web套接字连接。'*'允许任何源。 |  |
| <input type="checkbox" unchecked id="switch_0826"> | `remote-debugging-pipe` | `kRemoteDebuggingPipe` | 通过stdio管道[in=3, out=4]或通过'remote-debugging-io-pipes'开关中指定的远程管道启用远程调试。可选地，指定协议消息的格式，可以是"JSON"（默认）或"CBOR"。 |  |
| <input type="checkbox" unchecked id="switch_0827"> | `remote-debugging-port` | `kRemoteDebuggingPort` | 通过指定端口上的HTTP启用远程调试。 |  |
| <input type="checkbox" unchecked id="switch_0828"> | `renderer-client-id` | `kRendererClientId` |  |  |
| <input type="checkbox" unchecked id="switch_0829"> | `renderer-cmd-prefix` | `kRendererCmdPrefix` | 此标志的内容被添加到渲染器命令行的前面。有用的值可能是"valgrind"或"xterm -e gdb --args"。 |  |
| <input type="checkbox" unchecked id="switch_0830"> | `renderer-process-limit` | `kRendererProcessLimit` | 覆盖渲染器进程数量的默认/计算限制。此设置的非常高值可能导致高内存/资源使用或不稳定。 |  |
| <input type="checkbox" unchecked id="switch_0831"> | `renderer-startup-dialog` | `kRendererStartupDialog` | 使渲染器进程在启动时显示对话框。传递此标志还会在Windows非官方构建上添加sandbox::policy::kNoSandbox，因为这是显示对话框所需的。 |  |
| <input type="checkbox" unchecked id="switch_0832"> | `run-manual` | `kRunManualTestsFlag` | 手动测试仅在指定--run-manual时运行。这允许编写不自动运行但仍在同一测试二进制文件中的测试。这很有用，这样想要运行几个测试的团队不必添加必须在所有构建中编译的新二进制文件。 |  |
| <input type="checkbox" unchecked id="switch_0833"> | `sandbox-ipc` | `kSandboxIPCProcess` | 使进程作为沙盒IPC子进程运行。 |  |
| <input type="checkbox" unchecked id="switch_0834"> | `shared-array-buffer-unrestricted-access-allowed` | `kSharedArrayBufferUnrestrictedAccessAllowed` |  |  |
| <input type="checkbox" unchecked id="switch_0835"> | `shared-files` | `kSharedFiles` | 描述传递给子进程的文件描述符，采用以下列表格式：<file_id>:<descriptor_id>,<file_id>:<descriptor_id>,...其中<file_id>是正在启动的服务清单中的ID字符串，<descriptor_id>是子进程可以用来从全局描述符表检索文件描述符的描述符的数字标识符。 |  |
| <input type="checkbox" unchecked id="switch_0836"> | `single-process` | `kSingleProcess` | 在与浏览器相同的进程中运行渲染器和插件 |  |
| <input type="checkbox" unchecked id="switch_0837"> | `site-per-process` | `kSitePerProcess` | 强制执行一站点一进程安全策略：* 每个渲染器进程在其整个生命周期中专门为一个站点渲染页面。* 因此，来自不同站点的页面永远不会在同一进程中。* 渲染器进程的访问权限基于其站点受到限制。* 所有跨站点导航强制进程交换。* 每当src=是跨站点时，<iframe>都会在进程外渲染。更多详细信息：- https://www.chromium.org/developers/design-documents/site-isolation - https://www.chromium.org/developers/design-documents/process-models - site_instance.h中的类注释，列出了支持的进程模型。重要：这不要与--process-per-site混淆（后者是关于进程整合，而不是隔离）。您可能想要这个。 |  |
| <input type="checkbox" unchecked id="switch_0838"> | `skia-font-cache-limit-mb` | `kSkiaFontCacheLimitMb` | 指定skia字体缓存应使用的最大字节数。如果缓存需要分配更多内存，skia将清除以前的条目。 |  |
| <input type="checkbox" unchecked id="switch_0839"> | `skia-resource-cache-limit-mb` | `kSkiaResourceCacheLimitMb` | 指定skia资源缓存应使用的最大字节数。当内存使用超过此限制时，先前的条目将从缓存中清除。 |  |
| <input type="checkbox" unchecked id="switch_0840"> | `start-fullscreen` | `kStartFullscreen` | 指定浏览器是否应以全屏模式启动，就像用户在启动后立即按F11一样。 |  |
| <input type="checkbox" unchecked id="switch_0841"> | `target-device-scale-for-testing` | `kTargetDeviceScaleForTesting` | 允许Web测试为测试用例指定目标设备缩放。 |  |
| <input type="checkbox" unchecked id="switch_0842"> | `test-type` | `kTestType` | 当前测试工具的类型（"browser"或"ui"或"gpu"）。 |  |
| <input type="checkbox" unchecked id="switch_0843"> | `time-ticks-at-unix-epoch` | `kTimeTicksAtUnixEpoch` | 接受一个表示Unix纪元时的time-ticks值的数字。由于不同进程由于系统时钟更改可能为此产生不同的值，这允许将它们同步到单个值。 |  |
| <input type="checkbox" unchecked id="switch_0844"> | `touch-events` | `kTouchEventFeatureDetection` | 启用对触摸事件功能检测的支持。 |  |
| <input type="checkbox" unchecked id="switch_0845"> | `use-fake-codec-for-peer-connection` | `kUseFakeCodecForPeerConnection` | 用创建伪视频编码器和解码器的单个伪编解码器条目替换对等连接中支持的现有编解码器。 |  |
| <input type="checkbox" unchecked id="switch_0846"> | `use-fake-ui-for-digital-identity` | `kUseFakeUIForDigitalIdentity` | 绕过数字身份凭证OS调用。模拟用户接受OS呈现的对话框。 |  |
| <input type="checkbox" unchecked id="switch_0847"> | `use-fake-ui-for-fedcm` | `kUseFakeUIForFedCM` | 绕过FedCM账户选择对话框。如果为此开关提供值，则选择该账户ID，否则选择第一个账户。 |  |
| <input type="checkbox" unchecked id="switch_0848"> | `use-fake-ui-for-media-stream` | `kUseFakeUIForMediaStream` | 通过为媒体流（例如WebRTC）选择默认设备来绕过媒体流信息栏。与--use-fake-device-for-media-stream一起使用。首选--auto-accept-camera-and-microphone-capture，它不与屏幕/标签捕获交互。 |  |
| <input type="checkbox" unchecked id="switch_0849"> | `use-mock-cert-verifier-for-testing` | `kUseMockCertVerifierForTesting` | 使用MockCertVerifier。这仅在测试代码中有效。 |  |
| <input type="checkbox" unchecked id="switch_0850"> | `utility-cmd-prefix` | `kUtilityCmdPrefix` | 此标志的内容被添加到实用程序进程命令行的前面。有用的值可能是"valgrind"或"xterm -e gdb --args"。 |  |
| <input type="checkbox" unchecked id="switch_0851"> | `utility-immediate-crash-for-testing` | `kUtilityImmediateCrashForTesting` | 在启动早期使实用程序进程崩溃，用于测试。 |  |
| <input type="checkbox" unchecked id="switch_0852"> | `utility-startup-dialog` | `kUtilityStartupDialog` | 使实用程序进程在启动时显示对话框。 |  |
| <input type="checkbox" unchecked id="switch_0853"> | `utility-sub-type` | `kUtilitySubType` | 此开关指示实用程序进程的类型。它不影响进程提供的服务，但会添加到命令行中以便更容易识别实用程序进程的目的。 |  |
| <input type="checkbox" unchecked id="switch_0854"> | `v8-cache-options` | `kV8CacheOptions` | 设置缓存V8数据的选项。（none、code或default） |  |
| <input type="checkbox" unchecked id="switch_0855"> | `video-image-texture-target` | `kVideoImageTextureTarget` | CHROMIUM_image支持的视频帧纹理的纹理目标。 |  |
| <input type="checkbox" unchecked id="switch_0856"> | `wait-for-debugger-children` | `kWaitForDebuggerChildren` | 将kWaitForDebugger添加到每个子进程。如果传递了值，它将用作过滤器以确定子进程是否应传递kWaitForDebugger标志。 |  |
| <input type="checkbox" unchecked id="switch_0857"> | `wait-for-debugger-on-navigation` | `kWaitForDebuggerOnNavigation` | 在每次导航时，将记录带有渲染器URL的消息，渲染器将等待调试器附加或发送SIGUSR1以继续执行。 |  |
| <input type="checkbox" unchecked id="switch_0858"> | `wait-for-debugger-webui` | `kWaitForDebuggerWebUI` | WebUI测试运行器使用的标志，用于等待调试器附加。 |  |
| <input type="checkbox" unchecked id="switch_0859"> | `web-otp-backend` | `kWebOtpBackend` | 为Web OTP API启用指定的后端。 |  |
| <input type="checkbox" unchecked id="switch_0860"> | `web-otp-backend-auto` | `kWebOtpBackendAuto` | 为Web OTP API启用自动后端选择。 |  |
| <input type="checkbox" unchecked id="switch_0861"> | `web-otp-backend-sms-verification` | `kWebOtpBackendSmsVerification` | 为Web OTP API启用SMS验证后端，需要在SMS正文中包含应用哈希。 |  |
| <input type="checkbox" unchecked id="switch_0862"> | `web-otp-backend-user-consent` | `kWebOtpBackendUserConsent` | 为Web OTP API启用用户同意后端。 |  |
| <input type="checkbox" unchecked id="switch_0863"> | `web-settings-for-testing` | `kWebSettingsForTesting` | 允许Web测试为测试用例指定其他Web设置。 |  |
| <input type="checkbox" unchecked id="switch_0864"> | `webauthn-remote-desktop-support` | `kWebAuthRemoteDesktopSupport` | 允许受信任的远程桌面客户端代表其他来源进行WebAuthn请求。此开关仅控制remoteDesktopClientOverride扩展的可用性，但本身不启用任何来源使用它。 |  |
| <input type="checkbox" unchecked id="switch_0865"> | `webgl-antialiasing-mode` | `kWebglAntialiasingMode` | 设置用于WebGL的抗锯齿方法。（none、explicit、implicit） |  |
| <input type="checkbox" unchecked id="switch_0866"> | `webgl-msaa-sample-count` | `kWebglMSAASampleCount` | 如果启用了MSAA，为WebGL设置默认采样数。 |  |
| <input type="checkbox" unchecked id="switch_0867"> | `webrtc-event-logging` | `kWebRtcLocalEventLogging` | 启用WebRTC事件日志的捕获和本地存储，无需访问chrome://webrtc-internals。这对自动化测试很有用。它接受本地日志存储的路径。不重启浏览器并在没有此标志的情况下重新启动就无法禁用。 |  |
| <input type="checkbox" unchecked id="switch_0868"> | `zygote-cmd-prefix` | `kZygoteCmdPrefix` | 启动zygote进程时使用的前缀。（例如'gdb --args'） |  |

## Content Content Switches.cc, Policy (5 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0869"> | `gpu-process` | `kGpuProcess` | 使此进程成为GPU子进程。 |  |
| <input type="checkbox" unchecked id="switch_0870"> | `renderer` | `kRendererProcess` | 使进程作为渲染器而不是浏览器运行。 |  |
| <input type="checkbox" unchecked id="switch_0871"> | `type` | `kProcessType` | 此开关的值确定进程是作为渲染器还是插件主机启动。如果为空，则是浏览器。 |  |
| <input type="checkbox" unchecked id="switch_0872"> | `utility` | `kUtilityProcess` | 使进程作为实用程序子进程运行。 |  |
| <input type="checkbox" unchecked id="switch_0873"> | `zygote` | `kZygoteProcess` | 使进程作为zygote运行。 |  |

## Content Content Switches.cc, Ui Ui Switches.cc (3 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0874"> | `auto` | `kTouchEventFeatureDetectionAuto` | kTouchEventFeatureDetection开关可能具有的值，如--touch-events=disabled中所示。auto：存在附加触摸屏时在启动时启用。 |  |
| <input type="checkbox" unchecked id="switch_0875"> | `disabled` | `kTouchEventFeatureDetectionDisabled` | disabled：触摸事件已禁用。 |  |
| <input type="checkbox" unchecked id="switch_0876"> | `enabled` | `kTouchEventFeatureDetectionEnabled` | enabled：触摸事件始终启用。 |  |

## Crash (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0877"> | `crashpad-handler` | `kCrashpadHandler` | 一个进程类型（switches::kProcessType），指示chrome.exe或setup.exe作为crashpad_handler启动。这仅在Windows上使用。我们在Windows上将处理程序捆绑到chrome.exe中，因为"新"的.exe很可能被应用程序防火墙、防病毒软件等阻止或干扰。在其他平台上，crashpad_handler是一个独立的可执行文件。 |  |

## DBus (10 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0878"> | `attestation-server` | `kAttestationServer` | 在AttestationClient中用于确定使用哪个Google隐私CA进行证明。 |  |
| <input type="checkbox" unchecked id="switch_0879"> | `biod-fake` | `kBiodFake` | 启用BIOD虚假行为。如果设置了开关，将初始化虚假的biod D-Bus客户端，BIOD事件不会到达Chrome。 |  |
| <input type="checkbox" unchecked id="switch_0880"> | `cros-disks-fake` | `kCrosDisksFake` | 启用cros disks虚假行为。如果设置了开关，将初始化虚假的cros disk D-Bus客户端，USB事件不会到达Chrome。 |  |
| <input type="checkbox" unchecked id="switch_0881"> | `dbus-stub` | `kDbusStub` | 强制使用D-Bus客户端的stub实现。在非Chrome OS环境中使用stub D-Bus客户端是默认设置，要在非Chrome OS环境中使用真实的D-Bus客户端，请将此标志设置为"never"。 |  |
| <input type="checkbox" unchecked id="switch_0882"> | `fake-oobe-configuration-file` | `kFakeOobeConfiguration` | OOBE配置JSON文件的路径（由FakeOobeConfigurationClient使用）。 |  |
| <input type="checkbox" unchecked id="switch_0883"> | `hermes-fake` | `kHermesFake` | 启用Hermes虚假行为。默认情况下，不设置运营商配置文件。如果为此开关传递值"on"，则hermes虚假将使用单个已安装的运营商配置文件初始化。在Shill中也会设置与运营商配置文件对应的虚假蜂窝服务。 |  |
| <input type="checkbox" unchecked id="switch_0884"> | `register-max-dark-suspend-delay` | `kRegisterMaxDarkSuspendDelay` | 使Chrome在Chrome OS上注册最大可能的深度暂停延迟，即在深度恢复中给设备最大允许的时间来执行其工作。 |  |
| <input type="checkbox" unchecked id="switch_0885"> | `shill-stub` | `kShillStub` | 覆盖Shill stub行为。默认情况下，以太网、wifi和vpn已启用，转换会立即发生。多个选项可以用逗号分隔（无空格）。注意：所有选项都采用'foo=x'格式。值区分大小写，基于service_constants.h中的Shill名称。请参阅FakeShillManagerClient::SetInitialNetworkState的实现。示例：'clear=1' - 清除所有默认配置，'wifi=on' - wifi网络最初连接（'1'也有效），'wifi=off' - wifi网络最初全部断开连接（'0'也有效），'wifi=disabled' - wifi最初禁用，'wifi=none' - wifi不可用，'wifi=portal' - wifi连接将处于Portal状态，'cellular=1' - 蜂窝网络最初连接，'cellular=LTE' - 蜂窝网络最初连接，技术是LTE，'interactive=3' - 交互模式，连接/扫描等请求需要3秒。 |  |
| <input type="checkbox" unchecked id="switch_0886"> | `sms-test-messages` | `kSmsTestMessages` | 在首次调用RequestUpdate时发送测试消息（仅限stub）。 |  |
| <input type="checkbox" unchecked id="switch_0887"> | `system-developer-mode` | `kSystemDevMode` | FakeDebugDaemonClient使用，指定在Linux环境中运行时系统运行在开发模式。开发模式探测由会话管理器完成。 |  |

## Demo (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0888"> | `viz-demo-use-gpu` | `kVizDemoUseGPU` |  |  |

## Display (9 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0889"> | `ash-enable-software-mirroring` | `kEnableSoftwareMirroring` | 启用基于软件的镜像。 |  |
| <input type="checkbox" unchecked id="switch_0890"> | `ash-host-window-bounds` | `kHostWindowBounds` | 设置窗口大小、可选位置、可选缩放因子和可选面板圆角。"1024x768"创建大小为1024x768的窗口。"100+200-1024x768"将窗口定位在100,200。"1024x768*2"将缩放因子设置为2，适用于高DPI显示器。"1024x768~15\|15\|12\|12"设置面板角的半径为（左上=15px,右上=15px,右下=12px,左上=12px）。"800,0+800-800x800"用于两个800x800分辨率的显示器。"800,0+800-800x800,0+1600-800x800"用于三个800x800分辨率的显示器。 |  |
| <input type="checkbox" unchecked id="switch_0891"> | `ensure-forced-color-profile` | `kEnsureForcedColorProfile` | 如果显示器的颜色配置文件与强制颜色配置文件不匹配，在启动时崩溃浏览器。这在Mac上是必要的，因为Chrome的像素输出始终受到操作系统执行的颜色转换的影响。在所有其他平台上，这是无操作的。 |  |
| <input type="checkbox" unchecked id="switch_0892"> | `force-color-profile` | `kForceDisplayColorProfile` | 强制所有显示器被视为具有指定的颜色配置文件。接受的值为"srgb"和"generic-rgb"（目前由Mac布局测试使用）以及"color-spin-gamma24"（由布局测试使用）。 |  |
| <input type="checkbox" unchecked id="switch_0893"> | `force-device-scale-factor` | `kForceDeviceScaleFactor` | 覆盖浏览器UI和内容的设备缩放因子。 |  |
| <input type="checkbox" unchecked id="switch_0894"> | `force-raster-color-profile` | `kForceRasterColorProfile` | 强制栅格化在指定的颜色配置文件中进行。接受的值与上面的kForceDisplayColorProfile情况相同。 |  |
| <input type="checkbox" unchecked id="switch_0895"> | `screen-config` | `kScreenConfig` | 指定FakeDisplayDelegate的初始屏幕配置或所有显示器的状态，格式详细信息请参见类。 |  |
| <input type="checkbox" unchecked id="switch_0896"> | `secondary-display-layout` | `kSecondaryDisplayLayout` | 指定测试用的辅助显示器的布局模式和偏移。格式为"&lt;t\|r\|b\|l&gt;,&lt;offset&gt;"，其中t=TOP，r=RIGHT，b=BOTTOM，L=LEFT。例如，'r,-100'表示辅助显示器位于右侧，偏移量为-100。（位于主显示器上方） |  |
| <input type="checkbox" unchecked id="switch_0897"> | `use-first-display-as-internal` | `kUseFirstDisplayAsInternal` | 使用--ash-host-window-bounds中的第一个显示器作为内部显示器。这用于在Linux桌面上调试。 |  |

## Enterprise (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0898"> | `enable-chrome-browser-cloud-management` | `kEnableChromeBrowserCloudManagement` | 在Chromium构建中启用Chrome浏览器云管理集成。CBCM在品牌构建中始终启用。 |  |
| <input type="checkbox" unchecked id="switch_0899"> | `use-va-dev-keys` | `kUseVaDevKeys` |  |  |

## Events (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0900"> | `compensate-for-unstable-pinch-zoom` | `kCompensateForUnstablePinchZoom` | 启用不稳定捏合缩放的补偿。一些触摸屏在用手指沿直线移动时显示明显的抖动。这使得双指滚动触发振荡的捏合缩放。详见crbug.com/394380。 |  |
| <input type="checkbox" unchecked id="switch_0901"> | `touch-slop-distance` | `kTouchSlopDistance` | 覆盖手势检测的触摸倾斜距离。触摸倾斜距离是从触摸序列起始点开始，手势在不能再被视为点击之前可以移动的最大距离。滚动手势只能在移动了这个距离后开始。开关值是一个浮点数，被解释为像素距离。 |  |

## Extensions (27 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0902"> | `allow-future-manifest-version` | `kAllowFutureManifestVersion` |  |  |
| <input type="checkbox" unchecked id="switch_0903"> | `allow-http-background-page` | `kAllowHTTPBackgroundPage` |  |  |
| <input type="checkbox" unchecked id="switch_0904"> | `allow-legacy-extension-manifests` | `kAllowLegacyExtensionManifests` |  |  |
| <input type="checkbox" unchecked id="switch_0905"> | `allowlisted-extension-id` | `kAllowlistedExtensionID` |  |  |
| <input type="checkbox" unchecked id="switch_0906"> | `custom-action-iph` | `kZeroStatePromoCustomActionIph` |  |  |
| <input type="checkbox" unchecked id="switch_0907"> | `custom-ui-chip-iph` | `kZeroStatePromoCustomUiChipIph` |  |  |
| <input type="checkbox" unchecked id="switch_0908"> | `custom-ui-plain-link-iph` | `kZeroStatePromoCustomUiPlainLinkIph` |  |  |
| <input type="checkbox" unchecked id="switch_0909"> | `disable-app-content-verification` | `kDisableAppContentVerification` |  |  |
| <input type="checkbox" unchecked id="switch_0910"> | `disable-extensions` | `kDisableExtensions` | 禁用扩展。 |  |
| <input type="checkbox" unchecked id="switch_0911"> | `disable-extensions-except` | `kDisableExtensionsExcept` | 禁用扩展，除了在逗号分隔列表中指定的扩展。 |  |
| <input type="checkbox" unchecked id="switch_0912"> | `disable-extensions-file-access-check` | `kDisableExtensionsFileAccessCheck` |  |  |
| <input type="checkbox" unchecked id="switch_0913"> | `disable-extensions-http-throttling` | `kDisableExtensionsHttpThrottling` |  |  |
| <input type="checkbox" unchecked id="switch_0914"> | `embedded-extension-options` | `kEmbeddedExtensionOptions` |  |  |
| <input type="checkbox" unchecked id="switch_0915"> | `enable-ble-advertising-in-apps` | `kEnableBLEAdvertising` |  |  |
| <input type="checkbox" unchecked id="switch_0916"> | `enable-crx-hash-check` | `kEnableCrxHashCheck` |  |  |
| <input type="checkbox" unchecked id="switch_0917"> | `enable-experimental-extension-apis` | `kEnableExperimentalExtensionApis` |  |  |
| <input type="checkbox" unchecked id="switch_0918"> | `enable-trace-app-source` | `kTraceAppSource` |  |  |
| <input type="checkbox" unchecked id="switch_0919"> | `extension-process` | `kExtensionProcess` |  |  |
| <input type="checkbox" unchecked id="switch_0920"> | `extension-test-api-on-web-pages` | `kExtensionTestApiOnWebPages` |  |  |
| <input type="checkbox" unchecked id="switch_0921"> | `extension-zero-state-iph-variant` | `kZeroStatePromoIphVariantParamName` |  |  |
| <input type="checkbox" unchecked id="switch_0922"> | `extensions-on-chrome-urls` | `kExtensionsOnChromeURLs` |  |  |
| <input type="checkbox" unchecked id="switch_0923"> | `extensions-on-extension-urls` | `kExtensionsOnExtensionURLs` |  |  |
| <input type="checkbox" unchecked id="switch_0924"> | `load-apps` | `kLoadApps` |  |  |
| <input type="checkbox" unchecked id="switch_0925"> | `load-extension` | `kLoadExtension` |  |  |
| <input type="checkbox" unchecked id="switch_0926"> | `offscreen-document-testing` | `kOffscreenDocumentTesting` |  |  |
| <input type="checkbox" unchecked id="switch_0927"> | `set-extension-throttle-test-params` | `kSetExtensionThrottleTestParams` |  |  |
| <input type="checkbox" unchecked id="switch_0928"> | `show-component-extension-options` | `kShowComponentExtensionOptions` |  |  |

## Feedback (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0929"> | `feedback-server` | `kFeedbackServer` | 提交用户反馈时使用的替代反馈服务器 |  |

## Fuchsia (12 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0930"> | `cdm-data-directory` | `kCdmDataDirectory` |  |  |
| <input type="checkbox" unchecked id="switch_0931"> | `cdm-data-quota-bytes` | `kCdmDataQuotaBytes` |  |  |
| <input type="checkbox" unchecked id="switch_0932"> | `context-provider` | `kContextProvider` |  |  |
| <input type="checkbox" unchecked id="switch_0933"> | `cors-exempt-headers` | `kCorsExemptHeaders` |  |  |
| <input type="checkbox" unchecked id="switch_0934"> | `data-quota-bytes` | `kDataQuotaBytes` |  |  |
| <input type="checkbox" unchecked id="switch_0935"> | `enable-cast-streaming-receiver` | `kEnableCastStreamingReceiver` |  |  |
| <input type="checkbox" unchecked id="switch_0936"> | `enable-content-directories` | `kEnableContentDirectories` |  |  |
| <input type="checkbox" unchecked id="switch_0937"> | `enable-widevine` | `kEnableWidevine` |  |  |
| <input type="checkbox" unchecked id="switch_0938"> | `google-api-key` | `kGoogleApiKey` |  |  |
| <input type="checkbox" unchecked id="switch_0939"> | `playready-key-system` | `kPlayreadyKeySystem` |  |  |
| <input type="checkbox" unchecked id="switch_0940"> | `remote-debug-mode` | `kEnableRemoteDebugMode` |  |  |
| <input type="checkbox" unchecked id="switch_0941"> | `user-agent-product` | `kUserAgentProductAndVersion` |  |  |

## GCM (3 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0942"> | `gcm-checkin-url` | `kGCMCheckinURL` | 设置用于执行Google云消息服务签入的签入服务端点。 |  |
| <input type="checkbox" unchecked id="switch_0943"> | `gcm-mcs-endpoint` | `kGCMMCSEndpoint` | 设置用于Google云消息服务的移动连接服务器端点。 |  |
| <input type="checkbox" unchecked id="switch_0944"> | `gcm-registration-url` | `kGCMRegistrationURL` | 设置用于创建新的Google云消息服务注册的注册端点。 |  |

## Gaia (9 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0945"> | `gaia-config` | `kGaiaConfigPath` |  |  |
| <input type="checkbox" unchecked id="switch_0946"> | `gaia-config-contents` | `kGaiaConfigContents` |  |  |
| <input type="checkbox" unchecked id="switch_0947"> | `gaia-url` | `kGaiaUrl` |  |  |
| <input type="checkbox" unchecked id="switch_0948"> | `google-apis-url` | `kGoogleApisUrl` |  |  |
| <input type="checkbox" unchecked id="switch_0949"> | `google-url` | `kGoogleUrl` |  |  |
| <input type="checkbox" unchecked id="switch_0950"> | `lso-url` | `kLsoUrl` |  |  |
| <input type="checkbox" unchecked id="switch_0951"> | `oauth-account-manager-url` | `kOAuthAccountManagerUrl` |  |  |
| <input type="checkbox" unchecked id="switch_0952"> | `oauth2-client-id` | `kOAuth2ClientID` |  |  |
| <input type="checkbox" unchecked id="switch_0953"> | `oauth2-client-secret` | `kOAuth2ClientSecret` |  |  |

## Gamepad (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0954"> | `gamepad-polling-interval` | `kGamepadPollingInterval` | 覆盖手柄轮询间隔。减少间隔可以改善按钮和轴的输入延迟，但由于在输入轮询线程中花费更多CPU时间，可能会对性能产生负面影响。 |  |

## Gpu Command Buffer Client Gpu Switches.cc (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0955"> | `enable-gpu-client-logging` | `kEnableGPUClientLogging` | 启用GPU客户端日志记录。 |  |
| <input type="checkbox" unchecked id="switch_0956"> | `enable-gpu-client-tracing` | `kEnableGpuClientTracing` | 为渲染器中的GL调用启用TRACE。 |  |

## Gpu Command Buffer Service Gpu Switches.cc (19 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0957"> | `compile-shader-always-succeeds` | `kCompileShaderAlwaysSucceeds` | 编译着色器时始终返回成功。链接仍然会失败。 |  |
| <input type="checkbox" unchecked id="switch_0958"> | `disable-gl-error-limit` | `kDisableGLErrorLimit` | 禁用GL错误日志限制。 |  |
| <input type="checkbox" unchecked id="switch_0959"> | `disable-glsl-translator` | `kDisableGLSLTranslator` | 禁用GLSL转换器。 |  |
| <input type="checkbox" unchecked id="switch_0960"> | `disable-gpu-program-cache` | `kDisableGpuProgramCache` | 关闭GPU程序缓存。 |  |
| <input type="checkbox" unchecked id="switch_0961"> | `disable-gpu-shader-disk-cache` | `kDisableGpuShaderDiskCache` | 禁用GPU着色器磁盘缓存。 |  |
| <input type="checkbox" unchecked id="switch_0962"> | `disable-shader-name-hashing` | `kDisableShaderNameHashing` | 关闭着色器中的用户定义名称哈希。 |  |
| <input type="checkbox" unchecked id="switch_0963"> | `disable-vulkan-surface` | `kDisableVulkanSurface` | 禁用VK_KHR_surface扩展。将使用bitblt而不是交换链在屏幕上显示渲染结果。 |  |
| <input type="checkbox" unchecked id="switch_0964"> | `enable-gpu-command-logging` | `kEnableGPUCommandLogging` | 启用GPU命令日志记录。 |  |
| <input type="checkbox" unchecked id="switch_0965"> | `enable-gpu-debugging` | `kEnableGPUDebugging` | 启用每个命令后调用GL错误检查。 |  |
| <input type="checkbox" unchecked id="switch_0966"> | `enable-gpu-driver-debug-logging` | `kEnableGPUDriverDebugLogging` | 启用GPU驱动程序调试消息的日志记录。 |  |
| <input type="checkbox" unchecked id="switch_0967"> | `enable-threaded-texture-mailboxes` | `kEnableThreadedTextureMailboxes` | 当共享组不可用时模拟共享纹理。并非在所有地方都可用。 |  |
| <input type="checkbox" unchecked id="switch_0968"> | `enforce-gl-minimums` | `kEnforceGLMinimums` | 强制执行GL最小值。 |  |
| <input type="checkbox" unchecked id="switch_0969"> | `force-gpu-mem-discardable-limit-mb` | `kForceGpuMemDiscardableLimitMb` | 设置用于可丢弃缓存的最大GPU内存。 |  |
| <input type="checkbox" unchecked id="switch_0970"> | `force-max-texture-size` | `kForceMaxTextureSize` | 设置最大纹理大小（像素）。 |  |
| <input type="checkbox" unchecked id="switch_0971"> | `gl-shader-interm-output` | `kGLShaderIntermOutput` | 在着色器编译信息日志中包含ANGLE的中间表示（AST）输出。 |  |
| <input type="checkbox" unchecked id="switch_0972"> | `gpu-program-cache-size-kb` | `kGpuProgramCacheSizeKb` | 设置内存中GPU程序缓存的最大大小（KB）。 |  |
| <input type="checkbox" unchecked id="switch_0973"> | `native` | `kVulkanImplementationNameNative` |  |  |
| <input type="checkbox" unchecked id="switch_0974"> | `swiftshader` | `kVulkanImplementationNameSwiftshader` |  |  |
| <input type="checkbox" unchecked id="switch_0975"> | `use-vulkan` | `kUseVulkan` | 启用Vulkan支持并选择Vulkan实现，还必须定义ENABLE_VULKAN。这仅初始化Vulkan，还必须使用标志--enable-features=Vulkan来选择Vulkan进行合成和光栅化。 |  |

## Gpu Command Buffer Service Gpu Switches.cc, Ui Gl Gl Switches.cc (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0976"> | `enable-gpu-service-logging` | `kEnableGPUServiceLoggingGPU` | 启用GPU服务日志记录。注意：这与gl_switches.cc中的开关相同。为了避免DLL之间的依赖关系，在此再次定义。 |  |

## Gpu Config Gpu Switches.cc (47 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_0977"> | `collect-dawn-info-eagerly` | `kCollectDawnInfoEagerly` | 浏览器启动后立即启动GPU进程进行Dawn信息收集。默认延迟120秒。 |  |
| <input type="checkbox" unchecked id="switch_0978"> | `dawn` | `kSkiaGraphiteBackendDawn` |  |  |
| <input type="checkbox" unchecked id="switch_0979"> | `dawn-d3d11` | `kSkiaGraphiteBackendDawnD3D11` |  |  |
| <input type="checkbox" unchecked id="switch_0980"> | `dawn-d3d12` | `kSkiaGraphiteBackendDawnD3D12` |  |  |
| <input type="checkbox" unchecked id="switch_0981"> | `dawn-metal` | `kSkiaGraphiteBackendDawnMetal` |  |  |
| <input type="checkbox" unchecked id="switch_0982"> | `dawn-swiftshader` | `kSkiaGraphiteBackendDawnSwiftshader` |  |  |
| <input type="checkbox" unchecked id="switch_0983"> | `dawn-vulkan` | `kSkiaGraphiteBackendDawnVulkan` |  |  |
| <input type="checkbox" unchecked id="switch_0984"> | `disable-dawn-features` | `kDisableDawnFeatures` | 在创建Dawn设备时设置禁用的Dawn功能（切换）。 |  |
| <input type="checkbox" unchecked id="switch_0985"> | `disable-gpu-process-for-dx12-info-collection` | `kDisableGpuProcessForDX12InfoCollection` | 禁用用于DX12信息收集的非沙盒GPU进程。 |  |
| <input type="checkbox" unchecked id="switch_0986"> | `disable-gpu-rasterization` | `kDisableGpuRasterization` | 禁用GPU光栅化，即仅在CPU上光栅化。覆盖kEnableGpuRasterization标志。 |  |
| <input type="checkbox" unchecked id="switch_0987"> | `disable-mipmap-generation` | `kDisableMipmapGeneration` | 在Skia中禁用mipmap生成。用作某些低内存设备的解决方法，详见https://crbug.com/1138979。 |  |
| <input type="checkbox" unchecked id="switch_0988"> | `disable-skia-graphite` | `kDisableSkiaGraphite` | 强制禁用/启用Skia Graphite。如果同时指定，禁用将优先于启用。 |  |
| <input type="checkbox" unchecked id="switch_0989"> | `disable-skia-graphite-precompilation` | `kDisableSkiaGraphitePrecompilation` | 强制禁用/启用Skia Graphite的管道预编译。如果同时指定，禁用将优先于启用。 |  |
| <input type="checkbox" unchecked id="switch_0990"> | `disable-vulkan-fallback-to-gl-for-testing` | `kDisableVulkanFallbackToGLForTesting` | 禁用在Vulkan初始化失败时回退到基于GL的硬件渲染。这允许测试捕获Vulkan中的回归。 |  |
| <input type="checkbox" unchecked id="switch_0991"> | `enable-dawn-backend-validation` | `kEnableDawnBackendValidation` | 在Dawn后端启用验证层。 |  |
| <input type="checkbox" unchecked id="switch_0992"> | `enable-dawn-features` | `kEnableDawnFeatures` | 在创建Dawn设备时设置启用的Dawn功能（切换）。 |  |
| <input type="checkbox" unchecked id="switch_0993"> | `enable-gpu-blocked-time` | `kEnableGpuBlockedTime` | 启用测量GPU主线程在SwapBuffers之间被阻塞的时间长度。 |  |
| <input type="checkbox" unchecked id="switch_0994"> | `enable-gpu-main-time-keeper-metrics` | `kEnableGpuMainTimeKeeperMetrics` | 使用CrGpuMain作为后缀启用ThreadControllerWithMessagePumpImpl的TimeKeeper UMA指标。 |  |
| <input type="checkbox" unchecked id="switch_0995"> | `enable-gpu-rasterization` | `kEnableGpuRasterization` | 允许启发式方法确定何时应使用Skia GPU后端绘制图层瓦片。仅在GPU加速合成时有效。 |  |
| <input type="checkbox" unchecked id="switch_0996"> | `enable-skia-graphite` | `kEnableSkiaGraphite` |  |  |
| <input type="checkbox" unchecked id="switch_0997"> | `enable-skia-graphite-precompilation` | `kEnableSkiaGraphitePrecompilation` |  |  |
| <input type="checkbox" unchecked id="switch_0998"> | `enable-unsafe-webgpu` | `kEnableUnsafeWebGPU` |  |  |
| <input type="checkbox" unchecked id="switch_0999"> | `enable-vulkan-protected-memory` | `kEnableVulkanProtectedMemory` | 启用为Vulkan资源使用受保护的内存。 |  |
| <input type="checkbox" unchecked id="switch_1000"> | `enable-webgpu-developer-features` | `kEnableWebGPUDeveloperFeatures` | 启用通常不向Web平台公开的WebGPU开发者功能。 |  |
| <input type="checkbox" unchecked id="switch_1001"> | `force-browser-crash-on-gpu-crash` | `kForceBrowserCrashOnGpuCrash` | 如果GPU进程崩溃，使Chrome崩溃。这是为了在GPU进程意外崩溃时强制测试失败。 |  |
| <input type="checkbox" unchecked id="switch_1002"> | `force-high-performance-gpu` | `kForceHighPerformanceGPU` |  |  |
| <input type="checkbox" unchecked id="switch_1003"> | `force-separate-egl-display-for-webgl-testing` | `kForceSeparateEGLDisplayForWebGLTesting` | 强制为WebGL上下文使用单独的EGL显示。用于在只有一个有效GPU的设备上测试多GPU路径。 |  |
| <input type="checkbox" unchecked id="switch_1004"> | `force-webgpu-compat` | `kForceWebGPUCompat` | 强制所有WebGPU内容在WebGPU兼容模式下运行。 |  |
| <input type="checkbox" unchecked id="switch_1005"> | `gpu-blocklist-test-group` | `kGpuBlocklistTestGroup` | 选择具有指定test_group ID的不同GPU阻止列表条目集。 |  |
| <input type="checkbox" unchecked id="switch_1006"> | `gpu-device-id` | `kGpuDeviceId` | 将活动图形设备ID从浏览器进程传递到信息收集GPU进程。 |  |
| <input type="checkbox" unchecked id="switch_1007"> | `gpu-disk-cache-size-kb` | `kGpuDiskCacheSizeKB` | 允许为嵌入式设备明确指定着色器磁盘缓存大小。默认值为6MB。在Android上，默认为2MB，低端设备为128KB。 |  |
| <input type="checkbox" unchecked id="switch_1008"> | `gpu-driver-bug-list-test-group` | `kGpuDriverBugListTestGroup` | 启用具有指定test_group ID的额外GPU驱动程序错误列表条目集。注意默认测试组（组0）仍然活动。 |  |
| <input type="checkbox" unchecked id="switch_1009"> | `gpu-driver-version` | `kGpuDriverVersion` | 将活动图形驱动程序版本从浏览器进程传递到信息收集GPU进程。 |  |
| <input type="checkbox" unchecked id="switch_1010"> | `gpu-preferences` | `kGpuPreferences` | 将编码的GpuPreferences传递给GPU进程。 |  |
| <input type="checkbox" unchecked id="switch_1011"> | `gpu-revision` | `kGpuRevision` | 将活动图形修订信息从浏览器进程传递到信息收集GPU进程。 |  |
| <input type="checkbox" unchecked id="switch_1012"> | `gpu-sub-system-id` | `kGpuSubSystemId` | 将活动图形子系统ID从浏览器进程传递到信息收集GPU进程。 |  |
| <input type="checkbox" unchecked id="switch_1013"> | `gpu-vendor-id` | `kGpuVendorId` | 将活动图形供应商ID从浏览器进程传递到信息收集GPU进程。 |  |
| <input type="checkbox" unchecked id="switch_1014"> | `gpu-watchdog-timeout-seconds` | `kGpuWatchdogTimeoutSeconds` | GPU看门狗超时的覆盖值（秒）。 |  |
| <input type="checkbox" unchecked id="switch_1015"> | `ignore-gpu-blocklist` | `kIgnoreGpuBlocklist` | 忽略GPU阻止列表。 |  |
| <input type="checkbox" unchecked id="switch_1016"> | `metal` | `kSkiaGraphiteBackendMetal` |  |  |
| <input type="checkbox" unchecked id="switch_1017"> | `no-delay-for-dx12-vulkan-info-collection` | `kNoDelayForDX12VulkanInfoCollection` | 浏览器启动后立即启动用于DX12和Vulkan信息收集的非沙盒GPU进程。默认延迟120秒。 |  |
| <input type="checkbox" unchecked id="switch_1018"> | `skia-graphite-backend` | `kSkiaGraphiteBackend` | 指定Skia Graphite使用的后端 - "dawn"（默认）或"metal"（仅在非官方开发者构建中允许）。 |  |
| <input type="checkbox" unchecked id="switch_1019"> | `suppress-performance-logs` | `kSuppressPerformanceLogs` | 抑制可能发送到JS控制台并因测试输出日志期望比较而导致不必要测试失败的GL_DEBUG_TYPE_PERFORMANCE日志消息。 |  |
| <input type="checkbox" unchecked id="switch_1020"> | `use-redist-dml` | `kUseRedistributableDirectML` | 尝试使用可再分发的DirectML.dll。用于在WebNN集成到Windows OS之前对较新的DirectML版本进行测试。请参见DirectML版本的更多信息：https://learn.microsoft.com/en-us/windows/ai/directml/dml-version-history |  |
| <input type="checkbox" unchecked id="switch_1021"> | `vulkan-heap-memory-limit-mb` | `kVulkanHeapMemoryLimitMb` | 指定Vulkan内存的堆限制。TODO(crbug.com/40161102)：移除此开关。 |  |
| <input type="checkbox" unchecked id="switch_1022"> | `vulkan-sync-cpu-memory-limit-mb` | `kVulkanSyncCpuMemoryLimitMb` | 指定总Vulkan内存的同步CPU限制。TODO(crbug.com/40161102)：移除此开关。 |  |
| <input type="checkbox" unchecked id="switch_1023"> | `webview-draw-functor-uses-vulkan` | `kWebViewDrawFunctorUsesVulkan` | 指示这正在被Android WebView使用，其绘制函数使用Vulkan。 |  |

## Gpu Config Gpu Switches.h (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1024"> | `use-webgpu-adapter` | `kUseWebGPUAdapter` |  |  |
| <input type="checkbox" unchecked id="switch_1025"> | `use-webgpu-power-preference` | `kUseWebGPUPowerPreference` |  |  |

## Graphics (5 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1026"> | `animation-duration-scale` | `kAnimationDurationScale` | 应用于每个动画持续时间的缩放因子。必须 >= 0.0。这仅适用于LinearAnimation及其子类。 |  |
| <input type="checkbox" unchecked id="switch_1027"> | `disable-font-subpixel-positioning` | `kDisableFontSubpixelPositioning` | 强制禁用字体子像素定位。这影响字符字形锐度、字距调整、提示和布局。 |  |
| <input type="checkbox" unchecked id="switch_1028"> | `enable-native-gpu-memory-buffers` | `kEnableNativeGpuMemoryBuffers` | 在Linux上启用原生CPU可映射的GPU内存缓冲区支持。 |  |
| <input type="checkbox" unchecked id="switch_1029"> | `force-prefers-no-reduced-motion` | `kForcePrefersNoReducedMotion` | 强制设置用户是否不希望减少运动，无论系统设置如何。 |  |
| <input type="checkbox" unchecked id="switch_1030"> | `force-prefers-reduced-motion` | `kForcePrefersReducedMotion` | 强制设置用户是否希望减少运动，无论系统设置如何。 |  |

## Graphics, Headless (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1031"> | `screen-info` | `kScreenInfo` | 无头屏幕信息格式：{0,0 800x600}{800,0 600x800}。详见//components/headless/screen_info/README.md。 |  |

## HID (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1032"> | `disable-hid-blocklist` | `kDisableHidBlocklist` | 禁用HID阻止列表。 |  |

## Headless (22 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1033"> | `allow-chrome-scheme-url` | `kAllowChromeSchemeUrl` | 允许无头模式访问任何方案为chrome://的URL。 |  |
| <input type="checkbox" unchecked id="switch_1034"> | `allow-video-codecs` | `kAllowVideoCodecs` | 允许的视频编解码器的逗号分隔、不区分大小写的列表。如果指定，不匹配列表的编解码器将不被使用。'*'将匹配所有内容，条目开头的'-'表示不允许编解码器。第一个匹配的条目决定结果。编解码器名称如media/base/video_codecs.cc中GetCodecName()返回的。 |  |
| <input type="checkbox" unchecked id="switch_1035"> | `block-new-web-contents` | `kBlockNewWebContents` | 如果为true，则所有弹出窗口和对window.open的调用都将失败。 |  |
| <input type="checkbox" unchecked id="switch_1036"> | `default-background-color` | `kDefaultBackgroundColor` | 如果页面未指定背景色，则使用的背景色。以十六进制RGB或RGBA整数值提供，例如'ff0000ff'表示红色或'00000000'表示透明。 |  |
| <input type="checkbox" unchecked id="switch_1037"> | `deterministic-mode` | `kDeterministicMode` | 元标志。这设置了许多标志，将浏览器置于确定性模式，其中应通过DevToolsProtocol（实验性）发出开始帧。 |  |
| <input type="checkbox" unchecked id="switch_1038"> | `disable-cookie-encryption` | `kDisableCookieEncryption` | 作为用户配置文件一部分存储的Cookie是否已加密。 |  |
| <input type="checkbox" unchecked id="switch_1039"> | `disable-pdf-tagging` | `kDisablePDFTagging` | 打印PDF时不发出标签。 |  |
| <input type="checkbox" unchecked id="switch_1040"> | `dump-dom` | `kDumpDom` | 将序列化的DOM（doctype + document.documentElement.outerHTML）打印到stdout。 |  |
| <input type="checkbox" unchecked id="switch_1041"> | `enable-begin-frame-control` | `kEnableBeginFrameControl` | 是否应通过DevToolsProtocol（实验性）发出开始帧。 |  |
| <input type="checkbox" unchecked id="switch_1042"> | `enable-bfcache` | `kEnableBackForwardCache` | 启用后退前进缓存支持。 |  |
| <input type="checkbox" unchecked id="switch_1043"> | `enable-gpu` | `kEnableGPU` | 启用硬件GPU支持。无头模式默认使用SwiftShader以确保无头环境间的一致性。此标志只是关闭SwiftShader的强制使用，让我们回到常规驱动选择逻辑。或者，可以使用--use-gl或--use-angle强制特定驱动程序。两种方法都不保证启用硬件GPU支持，因为这仍然取决于无头模式是否可以访问X显示等。 |  |
| <input type="checkbox" unchecked id="switch_1044"> | `font-render-hinting` | `kFontRenderHinting` | 运行无头模式时设置字体渲染提示，影响Skia渲染以及是否启用字形子像素定位。可能值：none\|slight\|medium\|full\|max。默认：full。 |  |
| <input type="checkbox" unchecked id="switch_1045"> | `force-new-browsing-instance` | `kForceNewBrowsingInstance` | 强制每次导航使用新的BrowsingInstance。 |  |
| <input type="checkbox" unchecked id="switch_1046"> | `force-reporting-destination-attested` | `kForceReportingDestinationAttested` | 为无头shell强制报告目标已验证。 |  |
| <input type="checkbox" unchecked id="switch_1047"> | `generate-pdf-document-outline` | `kGeneratePDFDocumentOutline` | 将文档大纲嵌入到打印的PDF中。 |  |
| <input type="checkbox" unchecked id="switch_1048"> | `no-pdf-header-footer` | `kNoPDFHeaderFooter` | 在打印的PDF文件中不显示页眉和页脚。 |  |
| <input type="checkbox" unchecked id="switch_1049"> | `no-system-proxy-config-service` | `kNoSystemProxyConfigService` | 不使用系统代理配置服务。 |  |
| <input type="checkbox" unchecked id="switch_1050"> | `password-store` | `kPasswordStore` | 指定使用哪个加密存储后端。可能值为kwallet、kwallet5、gnome-libsecret、basic。任何其他值将导致Chrome自动检测最佳后端。TODO(crbug.com/40449930)：一旦PasswordStore不再使用KWallet存储密码，重命名此标志以停止引用密码。但不要过早重命名；开发人员和测试人员可能依靠它来将大量测试密码保留在其KWallets之外。 |  |
| <input type="checkbox" unchecked id="switch_1051"> | `print-to-pdf` | `kPrintToPDF` | 保存已加载页面的PDF文件。 |  |
| <input type="checkbox" unchecked id="switch_1052"> | `screenshot` | `kScreenshot` | 保存已加载页面的截图。 |  |
| <input type="checkbox" unchecked id="switch_1053"> | `timeout` | `kTimeout` | 在指定的毫秒数后发出停止。这将取消所有导航并导致触发DOMContentLoaded事件。 |  |
| <input type="checkbox" unchecked id="switch_1054"> | `virtual-time-budget` | `kVirtualTimeBudget` | 如果设置，系统等待指定数量的虚拟毫秒，然后认为页面已准备就绪。为了确定性，虚拟时间在有待处理的网络获取时不会推进（即不会触发计时器）。一旦所有网络获取完成，计时器触发，如果系统用完虚拟时间，则快进以便下一个计时器立即触发，直到指定的虚拟时间预算耗尽。 |  |

## Headless, Shell (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1055"> | `crash-dumps-dir` | `kCrashDumpsDir` | breakpad应存储minidumps的目录。 |  |

## Headless, Switches.cc (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1056"> | `enable-crash-reporter` | `kEnableCrashReporter` | 指示应启用崩溃报告。在辅助进程无法访问做出此决定所需文件的平台上，此标志由内部生成。 |  |

## I18n (4 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1057"> | `force-text-direction` | `kForceTextDirection` | 强制文本渲染到特定方向。有效值为"ltr"（从左到右）和"rtl"（从右到左）。仅与RTL进行了有意义的测试。 |  |
| <input type="checkbox" unchecked id="switch_1058"> | `force-ui-direction` | `kForceUIDirection` | 强制UI到特定方向。有效值为"ltr"（从左到右）和"rtl"（从右到左）。 |  |
| <input type="checkbox" unchecked id="switch_1059"> | `ltr` | `kForceDirectionLTR` |  |  |
| <input type="checkbox" unchecked id="switch_1060"> | `rtl` | `kForceDirectionRTL` |  |  |

## Infobars (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1061"> | `disable-infobars` | `kDisableInfoBars` |  |  |

## Input (3 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1062"> | `disable-hang-monitor` | `kDisableHangMonitor` | 抑制渲染器进程中的挂起监视器对话框。这可能允许页面上的慢卸载处理程序阻止标签页关闭，但在这种情况下可以使用任务管理器终止违规进程。 |  |
| <input type="checkbox" unchecked id="switch_1063"> | `disable-pinch` | `kDisablePinch` | 禁用合成器加速的触摸屏捏合手势。 |  |
| <input type="checkbox" unchecked id="switch_1064"> | `validate-input-event-stream` | `kValidateInputEventStream` | 在调试构建中，断言输入事件流是有效的。 |  |

## Keyboard (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1065"> | `disable-virtual-keyboard` | `kDisableVirtualKeyboard` |  |  |
| <input type="checkbox" unchecked id="switch_1066"> | `enable-virtual-keyboard` | `kEnableVirtualKeyboard` |  |  |

## Mahi (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1067"> | `use-fake-mahi-manager` | `kUseFakeMahiManager` | 在Mahi功能中使用虚假的MahiManager。显示上下文菜单时也总是显示Mahi菜单。 |  |

## Media Capture (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1068"> | `disable-video-capture-use-gpu-memory-buffer` | `kDisableVideoCaptureUseGpuMemoryBuffer` | 这用于由kVideoCaptureUseGpuMemoryBuffer控制的相同功能。kVideoCaptureUseGpuMemoryBuffer由chromeos覆盖设置。此标志是通过chrome://标志覆盖设置所必需的。chrome://flag#zero-copy-video-capture的行为如下；默认：遵守chromeos覆盖设置。启用：强制启用kVideoCaptureUseGpuMemoryBuffer。禁用：强制禁用kVideoCaptureUseGpuMemoryBuffer。 |  |
| <input type="checkbox" unchecked id="switch_1069"> | `video-capture-use-gpu-memory-buffer` | `kVideoCaptureUseGpuMemoryBuffer` | 启用基于GpuMemoryBuffer的缓冲池。 |  |

## Media Media Switches.cc (34 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1070"> | `audio-buffer-size` | `kAudioBufferSize` | 允许用户为调试目的指定自定义缓冲区大小。 |  |
| <input type="checkbox" unchecked id="switch_1071"> | `auto-grant-captured-surface-control-prompt` | `kAutoGrantCapturedSurfaceControlPrompt` | 跳过捕获表面控制的权限提示。 |  |
| <input type="checkbox" unchecked id="switch_1072"> | `autoplay-policy` | `kAutoplayPolicy` | 设置自动播放策略的命令行标志名称。 |  |
| <input type="checkbox" unchecked id="switch_1073"> | `cast-streaming-force-disable-hardware-h264` | `kCastStreamingForceDisableHardwareH264` |  |  |
| <input type="checkbox" unchecked id="switch_1074"> | `cast-streaming-force-disable-hardware-vp8` | `kCastStreamingForceDisableHardwareVp8` |  |  |
| <input type="checkbox" unchecked id="switch_1075"> | `cast-streaming-force-disable-hardware-vp9` | `kCastStreamingForceDisableHardwareVp9` |  |  |
| <input type="checkbox" unchecked id="switch_1076"> | `cast-streaming-force-enable-hardware-h264` | `kCastStreamingForceEnableHardwareH264` |  |  |
| <input type="checkbox" unchecked id="switch_1077"> | `cast-streaming-force-enable-hardware-vp8` | `kCastStreamingForceEnableHardwareVp8` |  |  |
| <input type="checkbox" unchecked id="switch_1078"> | `cast-streaming-force-enable-hardware-vp9` | `kCastStreamingForceEnableHardwareVp9` |  |  |
| <input type="checkbox" unchecked id="switch_1079"> | `clear-key-cdm-path-for-testing` | `kClearKeyCdmPathForTesting` | 指定用于测试的Clear Key CDM路径，这是在启用库CDM时支持外部Clear Key密钥系统所必需的。注意外部Clear Key密钥系统支持也由功能kExternalClearKeyForTesting控制。 |  |
| <input type="checkbox" unchecked id="switch_1080"> | `disable-accelerated-mjpeg-decode` | `kDisableAcceleratedMjpegDecode` | 禁用捕获帧的mjpeg解码硬件加速（如果可用）。 |  |
| <input type="checkbox" unchecked id="switch_1081"> | `disable-audio-input` | `kDisableAudioInput` | 强制输入和输出流创建使用虚假音频流。 |  |
| <input type="checkbox" unchecked id="switch_1082"> | `disable-audio-output` | `kDisableAudioOutput` |  |  |
| <input type="checkbox" unchecked id="switch_1083"> | `disable-background-media-suspend` | `kDisableBackgroundMediaSuspend` | 不立即挂起后台标签页中的媒体。 |  |
| <input type="checkbox" unchecked id="switch_1084"> | `disable-rtc-smoothness-algorithm` | `kDisableRTCSmoothnessAlgorithm` | 禁用为webrtc设计的新渲染算法，该算法旨在改善渲染平滑度。 |  |
| <input type="checkbox" unchecked id="switch_1085"> | `document-user-activation-required` | `kDocumentUserActivationRequiredPolicy` | 需要文档用户激活的自动播放策略。 |  |
| <input type="checkbox" unchecked id="switch_1086"> | `enable-live-caption-pref-for-testing` | `kEnableLiveCaptionPrefForTesting` | 将kLiveCaptionEnabled首选项的默认值设置为true。 |  |
| <input type="checkbox" unchecked id="switch_1087"> | `fail-audio-stream-creation` | `kFailAudioStreamCreation` | 使AudioManager创建音频流失败。用于测试各种失败情况。 |  |
| <input type="checkbox" unchecked id="switch_1088"> | `fake-background-blur-toggle-period` | `kFakeBackgroundBlurTogglePeriod` | 将虚假背景模糊状态插入VideoFrameMetadata。值表示周期（毫秒）。例如，设置为1000ms，将使模糊状态在报告ENABLED 500ms和DISABLED 500ms之间循环。 |  |
| <input type="checkbox" unchecked id="switch_1089"> | `force-video-overlays` | `kForceVideoOverlays` | 在Android上强制媒体播放器使用SurfaceView而不是SurfaceTexture。 |  |
| <input type="checkbox" unchecked id="switch_1090"> | `mse-audio-buffer-size-limit-mb` | `kMSEAudioBufferSizeLimitMb` | 允许明确指定MSE音频/视频缓冲区大小（兆字节）。默认值为视频150M，音频12M。 |  |
| <input type="checkbox" unchecked id="switch_1091"> | `mse-video-buffer-size-limit-mb` | `kMSEVideoBufferSizeLimitMb` |  |  |
| <input type="checkbox" unchecked id="switch_1092"> | `mute-audio` | `kMuteAudio` | 静音发送到音频设备的音频，以便在自动化测试期间不可听见。 |  |
| <input type="checkbox" unchecked id="switch_1093"> | `no-user-gesture-required` | `kNoUserGestureRequiredPolicy` | 不需要任何用户手势的自动播放策略。 |  |
| <input type="checkbox" unchecked id="switch_1094"> | `override-enabled-cdm-interface-version` | `kOverrideEnabledCdmInterfaceVersion` | 用此开关指定的版本覆盖默认启用的库CDM接口版本，这将是唯一启用的版本。例如，在支持（实现）CDM 8、CDM 9和CDM 10但默认仅启用CDM 8和CDM 9的构建中：--override-enabled-cdm-interface-version=8：仅启用CDM 8，--override-enabled-cdm-interface-version=9：仅启用CDM 9，--override-enabled-cdm-interface-version=10：仅启用CDM 10，--override-enabled-cdm-interface-version=11：不启用CDM接口。这可用于本地测试和调试。它还可用于在开发期间启用实验性CDM接口（默认总是禁用）进行测试。 |  |
| <input type="checkbox" unchecked id="switch_1095"> | `override-hardware-secure-codecs-for-testing` | `kOverrideHardwareSecureCodecsForTesting` | 覆盖硬件安全编解码器支持进行测试。如果指定，将跳过真实平台硬件安全编解码器检查。有效编解码器为：- 视频："vp8"、"vp9"、"avc1"、"hevc"、"dolbyvision"、"av01" - 不支持明文引导的视频：&lt;video&gt;-no-clearlead，其中&lt;video&gt;来自上述列表。- 音频："mp4a"、"vorbis"。编解码器用逗号分隔。例如：--override-hardware-secure-codecs-for-testing=vp8,vp9-no-clearlead,vorbis，--override-hardware-secure-codecs-for-testing=avc1,mp4a。假设指定的编解码器支持CENC加密方案。如果未指定有效编解码器，则不支持硬件安全编解码器。这可用于禁用硬件安全编解码器支持：--override-hardware-secure-codecs-for-testing |  |
| <input type="checkbox" unchecked id="switch_1096"> | `report-vp9-as-an-unsupported-mime-type` | `kReportVp9AsAnUnsupportedMimeType` | 强制将VP9报告为不受支持的MIME类型。 |  |
| <input type="checkbox" unchecked id="switch_1097"> | `unsafely-allow-protected-media-identifier-for-domain` | `kUnsafelyAllowProtectedMediaIdentifierForDomain` | 用于受保护内容的自动化测试，此开关允许特定域（例如example.com）始终允许共享受保护媒体标识符的权限。在此上下文中，域不包括端口号。启用此开关不会影响用户的内容设置。参考：http://crbug.com/718608。示例：--unsafely-allow-protected-media-identifier-for-domain=a.com,b.ca |  |
| <input type="checkbox" unchecked id="switch_1098"> | `use-fake-device-for-media-stream` | `kUseFakeDeviceForMediaStream` | 使用虚假设备替换实际摄像头和麦克风进行媒体流。有关允许参数的列表，请参见FakeVideoCaptureDeviceFactory::ParseFakeDevicesConfigFromOptionsString()。 |  |
| <input type="checkbox" unchecked id="switch_1099"> | `use-fake-mjpeg-decode-accelerator` | `kUseFakeMjpegDecodeAccelerator` | 使用虚假设备进行MJPEG的加速解码。这允许，例如，在不需要存在实际加速器硬件的情况下测试与GPU服务的通信。 |  |
| <input type="checkbox" unchecked id="switch_1100"> | `use-file-for-fake-audio-capture` | `kUseFileForFakeAudioCapture` | 播放.wav文件作为麦克风。注意对于WebRTC调用，我们会将比特视为来自麦克风，这意味着您应该禁用音频处理（否则您的音频文件将播放失真）。如有必要，输入文件会转换以适应Chrome的音频总线，因此大多数合理的.wav文件应该可以工作。您可以传递&lt;path&gt;循环播放文件或&lt;path&gt;%noloop在播放完成后停止。还必须与kDisableAudioInput或kUseFakeDeviceForMediaStream一起使用。 |  |
| <input type="checkbox" unchecked id="switch_1101"> | `use-file-for-fake-video-capture` | `kUseFileForFakeVideoCapture` | 使用.y4m文件作为网络摄像头播放。有关更多详细信息，请参见media/capture/video/file_video_capture_device.h中的注释。 |  |
| <input type="checkbox" unchecked id="switch_1102"> | `user-gesture-required` | `kUserGestureRequiredPolicy` | 需要用户手势才能播放的自动播放策略。 |  |
| <input type="checkbox" unchecked id="switch_1103"> | `video-threads` | `kVideoThreads` | 设置用于视频解码的线程数。 |  |

## Metrics (9 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1104"> | `export-uma-logs-to-file` | `kExportUmaLogsToFile` | 启用对会话期间创建的所有UMA日志的观察，并在关闭时自动将它们导出到传递的文件路径（如果文件不存在则创建文件）。这还启用在chrome://metrics-internals调试页面中查看所有UMA日志。导出文件的格式在MetricsServiceObserver::ExportLogsAsJson()中概述。用法示例：--export-uma-logs-to-file=/tmp/logs.json |  |
| <input type="checkbox" unchecked id="switch_1105"> | `force-enable-metrics-reporting` | `kForceEnableMetricsReporting` | 强制启用指标报告。不应用于测试，因为它会将数据发送到服务器。 |  |
| <input type="checkbox" unchecked id="switch_1106"> | `force-msbb-setting-on-for-ukm` | `kForceMsbbSettingOnForUkm` | 强制为UKM记录启用MSBB设置。应仅用于手动切换设置不可行或不实际的自动化测试浏览器会话中。 |  |
| <input type="checkbox" unchecked id="switch_1107"> | `metrics-recording-only` | `kMetricsRecordingOnly` | 启用指标报告的记录但禁用报告。与kForceEnableMetricsReporting相比，这执行普通客户端用于报告的所有代码，除了报告被丢弃而不是发送到服务器。这对于在UI和性能测试期间查找指标代码中的问题很有用。 |  |
| <input type="checkbox" unchecked id="switch_1108"> | `metrics-upload-interval` | `kMetricsUploadIntervalSec` | 覆盖UMA和UKM每次指标报告上传之间的标准时间间隔。设置为较短间隔对调试很有用。单位为秒。（桌面默认为1800秒）。 |  |
| <input type="checkbox" unchecked id="switch_1109"> | `reset-variation-state` | `kResetVariationState` | 强制重置此客户端上的一次性随机化FieldTrials，也称为Chrome变体状态。 |  |
| <input type="checkbox" unchecked id="switch_1110"> | `ukm-server-url` | `kUkmServerUrl` | 覆盖UKM报告上传到的服务器URL。这只能在调试构建中使用。 |  |
| <input type="checkbox" unchecked id="switch_1111"> | `uma-insecure-server-url` | `kUmaInsecureServerUrl` | 当连接到默认安全URL失败时，覆盖UMA报告上传到的服务器URL（参见|kUmaServerUrl|）。这只能在调试构建中使用。 |  |
| <input type="checkbox" unchecked id="switch_1112"> | `uma-server-url` | `kUmaServerUrl` | 覆盖UMA报告上传到的服务器URL。这只能在调试构建中使用。 |  |

## Modules (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1113"> | `signed-out-ntp-modules` | `kSignedOutNtpModulesSwitch` |  |  |

## Mojo (5 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1114"> | `attachment-name` | `kAttachmentName` | 对于期望单个具有分配给它的自由格式名称的Mojo邀请附件的客户端应用程序，这指定了该附件名称。必须在命令行上指定此项或kNumericAttachmentNames。 |  |
| <input type="checkbox" unchecked id="switch_1115"> | `host-ipcz-transport-fd` | `kHostIpczTransportFd` | mojo_proxy进程在被其主机启动时继承的文件描述符的整数值。此描述符引用连接到启动此代理以位于主机和某些传统客户端应用程序之间的主机进程的Unix套接字。必需。 |  |
| <input type="checkbox" unchecked id="switch_1116"> | `inherit-ipcz-broker` | `kInheritIpczBroker` | 默认情况下，mojo_proxy假设其主机是代理。给出此标志时，它假设其主机是提供共享其代理的非代理。代理必须在这方面正确配置，否则通过它的所有连接都将失败。 |  |
| <input type="checkbox" unchecked id="switch_1117"> | `legacy-client-fd` | `kLegacyClientFd` | mojo_proxy进程在被其主机启动时继承的文件描述符的整数值。此描述符引用连接到将成为此代理目标的传统客户端应用程序的Unix套接字。必需。 |  |
| <input type="checkbox" unchecked id="switch_1118"> | `num-attachments` | `kNumAttachments` | 对于期望Mojo邀请附件被分配基于零的64位整数值的客户端应用程序，这指定了正在使用的附件数量。名称隐含地是从0开始的顺序整数。 |  |

## Network Service (18 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1119"> | `additional-private-state-token-key-commitments` | `kAdditionalTrustTokenKeyCommitments` | 在网络服务中手动设置额外的私有状态令牌密钥承诺为给定值，该值应为满足TrustTokenKeyCommitmentParser::ParseMultipleIssuers要求的JSON字典。这些密钥除了通过TrustTokenKeyCommitments::Set最近调用提供的密钥外还可用。对于通过命令行和TrustTokenKeyCommitments::Set都提供密钥的发行者，通过命令行提供的密钥优先。这是因为手动测试的人可能希望通过命令行向启用了组件更新程序的真正Chrome发行版传递额外密钥，如果手动传递的密钥在启动后组件更新程序运行时被覆盖会令人惊讶。 |  |
| <input type="checkbox" unchecked id="switch_1120"> | `disable-shared-dictionary-storage-cleanup-for-testing` | `kDisableSharedDictionaryStorageCleanupForTesting` | 禁用共享字典存储清理任务的开关。仅用于测试。 |  |
| <input type="checkbox" unchecked id="switch_1121"> | `force-effective-connection-type` | `kForceEffectiveConnectionType` | 强制网络质量估算器(NQE)返回特定的有效连接类型。 |  |
| <input type="checkbox" unchecked id="switch_1122"> | `force-permission-policy-unload-default-enabled` | `kForcePermissionPolicyUnloadDefaultEnabled` | 如果设置，unload事件默认不能被权限策略禁用。 |  |
| <input type="checkbox" unchecked id="switch_1123"> | `host-resolver-rules` | `kHostResolverRules` | 这些映射仅适用于主机解析器。 |  |
| <input type="checkbox" unchecked id="switch_1124"> | `ignore-bad-message-for-testing` | `kIgnoreBadMessageForTesting` | 忽略错误mojo消息报告的开关。仅用于测试。 |  |
| <input type="checkbox" unchecked id="switch_1125"> | `ignore-certificate-errors-spki-list` | `kIgnoreCertificateErrorsSPKIList` | 一组用于忽略证书相关错误的公钥哈希。如果服务器提供的证书链验证失败，并且一个或多个证书的公钥哈希与此列表中的密钥匹配，则忽略错误。开关值必须是以逗号分隔的Base64编码SHA-256 SPKI指纹列表（RFC 7469，第2.4节）。除非同时存在--user-data-dir（由内容嵌入器定义），否则此开关无效。 |  |
| <input type="checkbox" unchecked id="switch_1126"> | `ip-address-space-overrides` | `kIpAddressSpaceOverrides` | 指定对IP端点 -&gt; IP地址空间映射的手动覆盖。这允许针对&quot;公共&quot;和&quot;本地&quot;IP地址运行本地测试。 此开关指定为逗号分隔的覆盖列表。每个覆盖作为冒号分隔的&quot;&lt;endpoint&gt;:&lt;address space&gt;&quot;对给出。 Grammar, in pseudo-BNF format: switch := override-list override-list := override “,” override-list \| &lt;nil&gt; override := ip-endpoint “=” address-space address-space := “public” \| “private” \| “local” \| &quot;loopback&quot; ip-endpoint := ip-address &quot;:&quot; port ip-address := see net::ParseURLHostnameToAddress() for details port := integer in the [0-65535] range Any invalid entries in the comma-separated list are ignored. If the port specified is 0, all ports for the given ip-address will be overridden. See also the design doc: https://docs.google.com/document/d/1-umCGylIOuSG02k9KGDwKayt3bzBXtGwVlCQHHkIcnQ/edit# And the Web Platform Test RFC #72 behind it: https://github.com/web-platform-tests/rfcs/blob/master/rfcs/address_space_overrides.md Note that since the doc and the RFC were written, the address space names have changed slightly due to Local Network Access (LNA) replacing Private Network Access (PNA). |  |
| <input type="checkbox" unchecked id="switch_1127"> | `log-net-log` | `kLogNetLog` | 启用将网络日志事件保存到文件。如果提供值，则将其用作文件路径，否则文件命名为netlog.json并放置在用户数据目录中。 |  |
| <input type="checkbox" unchecked id="switch_1128"> | `net-log-capture-mode` | `kNetLogCaptureMode` | 设置网络日志中要捕获事件的粒度。模式可以设置为以下值之一："Default" "IncludeSensitive" "Everything" 有关其含义的描述，请参见net_log_capture_mode.h中对应名称的枚举。 |  |
| <input type="checkbox" unchecked id="switch_1129"> | `net-log-duration` | `kLogNetLogDuration` | 指定网络日志记录的持续时间（秒）。当提供此标志并设置为正整数值X时，Chrome将在X秒后自动停止收集NetLog事件并将日志刷新到磁盘。 |  |
| <input type="checkbox" unchecked id="switch_1130"> | `net-log-max-size-mb` | `kNetLogMaxSizeMb` | 设置最大大小（以兆字节为单位）。日志文件在旧数据被覆盖之前可以增长到此大小。如果需要无限制的文件大小，请不要使用此标志。 |  |
| <input type="checkbox" unchecked id="switch_1131"> | `ssl-key-log-file` | `kSSLKeyLogFile` | 导致SSL密钥材料被记录到指定文件中用于调试目的。格式请参见https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/Key_Log_Format。 |  |
| <input type="checkbox" unchecked id="switch_1132"> | `store-probabilistic-reveal-tokens` | `kStoreProbabilisticRevealTokens` | The switch to enable storing probabilistic reveal tokens to disk. This should only be enabled for testing and debugging. |  |
| <input type="checkbox" unchecked id="switch_1133"> | `test-third-party-cookie-phaseout` | `kTestThirdPartyCookiePhaseout` |  |  |
| <input type="checkbox" unchecked id="switch_1134"> | `unsafely-treat-insecure-origin-as-secure` | `kUnsafelyTreatInsecureOriginAsSecure` | Treat given (insecure) origins as secure origins. Multiple origins can be supplied as a comma-separated list. For the definition of secure contexts, see https://w3c.github.io/webappsec-secure-contexts/ and https://www.w3.org/TR/powerful-features/#is-origin-trustworthy Example: --unsafely-treat-insecure-origin-as-secure=http://a.test,http://b.test |  |
| <input type="checkbox" unchecked id="switch_1135"> | `use-first-party-set` | `kUseFirstPartySet` | Allows the manual specification of a First-Party Set. The format is the same as that of --use-related-website-set. DEPRECATED(crbug.com/1486689): This switch is under deprecation due to renaming &quot;First-Party Set&quot; to &quot;Related Website Set&quot;. Please use kUseRelatedWebsiteSet instead. |  |
| <input type="checkbox" unchecked id="switch_1136"> | `use-related-website-set` | `kUseRelatedWebsiteSet` | Allows the manual specification of a Related Website Set. The set should be provided as a stringified JSON object, whose format matches the format of the JSON in https://github.com/GoogleChrome/related-website-sets. |  |

## Ozone (10 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1137"> | `disable-explicit-dma-fences` | `kDisableExplicitDmaFences` | 禁用显式DMA围栅。 |  |
| <input type="checkbox" unchecked id="switch_1138"> | `disable-wayland-ime` | `kDisableWaylandIme` | 禁用Wayland输入法编辑器。 |  |
| <input type="checkbox" unchecked id="switch_1139"> | `enable-wayland-ime` | `kEnableWaylandIme` | 尝试启用Wayland输入法编辑器。 |  |
| <input type="checkbox" unchecked id="switch_1140"> | `ozone-dump-file` | `kOzoneDumpFile` | 指定图像转储的位置。 |  |
| <input type="checkbox" unchecked id="switch_1141"> | `ozone-override-screen-size` | `kOzoneOverrideScreenSize` | 指定ozone屏幕大小。 |  |
| <input type="checkbox" unchecked id="switch_1142"> | `ozone-platform` | `kOzonePlatform` | 指定要使用的ozone平台实现。 |  |
| <input type="checkbox" unchecked id="switch_1143"> | `ozone-platform-hint` | `kOzonePlatformHint` | 建议要使用的ozone平台（仅限桌面Linux）。可以在chrome://flags上设置。参见https://crbug.com/1246928。 |  |
| <input type="checkbox" unchecked id="switch_1144"> | `render-node-override` | `kRenderNodeOverride` | 允许显式选择DRM渲染节点来创建用于渲染的gbm_device。 |  |
| <input type="checkbox" unchecked id="switch_1145"> | `use-wayland-explicit-grab` | `kUseWaylandExplicitGrab` | 打开弹出窗口时使用显式抓取。参见https://crbug.com/1220274 |  |
| <input type="checkbox" unchecked id="switch_1146"> | `wayland-text-input-version` | `kWaylandTextInputVersion` | 指定wayland文本输入协议版本。对于text-input-v1默认为"1"。可以指定值"3"以获得实验性text-input-v3支持。 |  |

## Permissions (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1147"> | `deny-permission-prompts` | `kDenyPermissionPrompts` | 通过拒绝而不是显示提示来阻止权限提示出现。 |  |

## Policy (19 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1148"> | `allow-sandbox-debugging` | `kAllowSandboxDebugging` | 允许调试沙盒进程（参见zygote_main_linux.cc）。 |  |
| <input type="checkbox" unchecked id="switch_1149"> | `code-sign-clone-cleanup` | `kCodeSignCloneCleanupProcessType` |  |  |
| <input type="checkbox" unchecked id="switch_1150"> | `device-management-url` | `kDeviceManagementUrl` | 指定与设备管理后端通信以获取配置策略和执行其他设备任务的URL。 |  |
| <input type="checkbox" unchecked id="switch_1151"> | `disable-gpu-sandbox` | `kDisableGpuSandbox` | 禁用GPU进程沙盒。 |  |
| <input type="checkbox" unchecked id="switch_1152"> | `disable-landlock-sandbox` | `kDisableLandlockSandbox` | 禁用Landlock沙盒（仅限Android）。 |  |
| <input type="checkbox" unchecked id="switch_1153"> | `disable-namespace-sandbox` | `kDisableNamespaceSandbox` | 禁用命名空间沙盒的使用。 |  |
| <input type="checkbox" unchecked id="switch_1154"> | `disable-seccomp-filter-sandbox` | `kDisableSeccompFilterSandbox` | 禁用seccomp过滤器沙盒（seccomp-bpf）（仅限Linux）。 |  |
| <input type="checkbox" unchecked id="switch_1155"> | `disable-setuid-sandbox` | `kDisableSetuidSandbox` | 禁用setuid沙盒（仅限Linux）。 |  |
| <input type="checkbox" unchecked id="switch_1156"> | `encrypted-reporting-url` | `kEncryptedReportingUrl` | 指定上传加密报告的URL。 |  |
| <input type="checkbox" unchecked id="switch_1157"> | `file-storage-server-upload-url` | `kFileStorageServerUploadUrl` | 指定与文件存储服务器（go/crosman-file-storage-server）通信以上传日志和支持包文件的URL。 |  |
| <input type="checkbox" unchecked id="switch_1158"> | `gpu-sandbox-allow-sysv-shm` | `kGpuSandboxAllowSysVShm` | 在GPU沙盒中允许shmat()系统调用。 |  |
| <input type="checkbox" unchecked id="switch_1159"> | `gpu-sandbox-failures-fatal` | `kGpuSandboxFailuresFatal` | 使GPU沙盒失败致命。 |  |
| <input type="checkbox" unchecked id="switch_1160"> | `no-sandbox` | `kNoSandbox` | 禁用通常被沙盒化的所有进程类型的沙盒。仅用作浏览器级测试开关。 |  |
| <input type="checkbox" unchecked id="switch_1161"> | `policy` | `kChromePolicy` | 通过命令行设置策略值。 |  |
| <input type="checkbox" unchecked id="switch_1162"> | `policy-verification-key` | `kPolicyVerificationKey` | 用命令行标志提供的密钥替换原始verification_key。只能用于单元测试或浏览器测试。 |  |
| <input type="checkbox" unchecked id="switch_1163"> | `realtime-reporting-url` | `kRealtimeReportingUrl` | 指定上传实时报告的URL。 |  |
| <input type="checkbox" unchecked id="switch_1164"> | `relauncher` | `kRelauncherProcessType` |  |  |
| <input type="checkbox" unchecked id="switch_1165"> | `secure-connect-api-url` | `kSecureConnectApiUrl` | 指定联系安全连接API的基础URL。 |  |
| <input type="checkbox" unchecked id="switch_1166"> | `service-sandbox-type` | `kServiceSandboxType` | 应用于运行服务的进程的沙盒类型，下一块中的值之一。 |  |

## Predictors (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1167"> | `loading-predictor-allow-local-request-for-testing` | `kLoadingPredictorAllowLocalRequestForTesting` | 允许加载预测器对本地IP地址进行预取。这对于测试是必需的，因为出于安全考虑，此类请求默认被阻止。 |  |

## Safe Browsing (21 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1168"> | `binary-upload-service-url` | `kCloudBinaryUploadServiceUrlFlag` |  |  |
| <input type="checkbox" unchecked id="switch_1169"> | `csd-debug-feature-directory` | `kCsdDebugFeatureDirectoryFlag` | Command-line flag that can be used to write extracted CSD features to disk. This is also enables a few other behaviors that are useful for debugging. |  |
| <input type="checkbox" unchecked id="switch_1170"> | `csd-model-override-path` | `kOverrideCsdModelFlag` | Command-line flag that can be used to override the current CSD model. Must be provided with an absolute path. |  |
| <input type="checkbox" unchecked id="switch_1171"> | `mark_as_allowlisted_for_phish_guard` | `kMarkAsPasswordProtectionAllowlisted` | List of comma-separated URLs to mark as present on the password protection allowlist. Note this uses the client-side detection allowlist. |  |
| <input type="checkbox" unchecked id="switch_1172"> | `mark_as_allowlisted_for_real_time` | `kMarkAsHighConfidenceAllowlisted` | List of comma-separated URLs to mark as present on the high-confidence allowlist. |  |
| <input type="checkbox" unchecked id="switch_1173"> | `mark_as_enterprise_blocked` | `kArtificialCachedEnterpriseBlockedVerdictFlag` | Command-line flag for caching an artificial blocked enterprise lookup verdict. |  |
| <input type="checkbox" unchecked id="switch_1174"> | `mark_as_enterprise_warned` | `kArtificialCachedEnterpriseWarnedVerdictFlag` | Command-line flag for caching an artificial flagged enterprise lookup verdict. |  |
| <input type="checkbox" unchecked id="switch_1175"> | `mark_as_hash_prefix_real_time_phishing` | `kArtificialCachedHashPrefixRealTimeVerdictFlag` | Command-line flag for caching an artificial phishing verdict for hash-prefix real-time lookups. |  |
| <input type="checkbox" unchecked id="switch_1176"> | `mark_as_malware` | `kMarkAsMalware` | List of comma-separated URLs to mark as malware for local database checks. |  |
| <input type="checkbox" unchecked id="switch_1177"> | `mark_as_phish_guard_phishing` | `kArtificialCachedPhishGuardVerdictFlag` | Command-line flag for caching an artificial PhishGuard unsafe verdict. |  |
| <input type="checkbox" unchecked id="switch_1178"> | `mark_as_phishing` | `kMarkAsPhishing` | List of comma-separated URLs to mark as phishing for local database checks. |  |
| <input type="checkbox" unchecked id="switch_1179"> | `mark_as_real_time_phishing` | `kArtificialCachedUrlRealTimeVerdictFlag` | Command-line flag for caching an artificial phishing verdict for URL real-time lookups. |  |
| <input type="checkbox" unchecked id="switch_1180"> | `mark_as_uws` | `kMarkAsUws` | List of comma-separated URLs to mark as unwanted software for local database checks. |  |
| <input type="checkbox" unchecked id="switch_1181"> | `safe-browsing-skip-csd-allowlist` | `kSkipCSDAllowlistOnPreclassification` | If present, indicates that the client-side detection allowlist check should be skipped (it is treated as no match). |  |
| <input type="checkbox" unchecked id="switch_1182"> | `safe-browsing-skip-high-confidence-allowlist` | `kSkipHighConfidenceAllowlist` | If the switch is present, any high-confidence allowlist check will return that it does not match the allowlist. |  |
| <input type="checkbox" unchecked id="switch_1183"> | `safe-browsing-treat-user-as-advanced-protection` | `kForceTreatUserAsAdvancedProtection` |  |  |
| <input type="checkbox" unchecked id="switch_1184"> | `safebrowsing-enable-enhanced-protection` | `kSbEnableEnhancedProtection` | 启用安全浏览增强保护。 |  |
| <input type="checkbox" unchecked id="switch_1185"> | `safebrowsing-manual-download-blacklist` | `kSbManualDownloadBlocklist` | List of comma-separated sha256 hashes of executable files which the download-protection service should treat as &quot;dangerous.&quot;  For a file to show a warning, it also must be considered a dangerous filetype and not be allowlisted otherwise (by signature or URL) and must be on a supported OS. Hashes are in hex. This is used for manual testing when looking for ways to by-pass download protection. |  |
| <input type="checkbox" unchecked id="switch_1186"> | `url-filtering-endpoint` | `kUrlFilteringEndpointFlag` | Alternate URL to use for ChromeEnterpriseRealTimeUrlLookupService real-time lookups. |  |
| <input type="checkbox" unchecked id="switch_1187"> | `wp-max-file-opening-threads` | `kWpMaxFileOpeningThreads` |  |  |
| <input type="checkbox" unchecked id="switch_1188"> | `wp-max-parallel-active-requests` | `kWpMaxParallelActiveRequests` | 控制最大并发活动请求数量的命令行标志。 |  |

## Services Resource Coordinator Memory Instrumentation Switches.cc (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1189"> | `disable-chrome-tracing-computation` | `kDisableChromeTracingComputation` | 在写入跟踪时禁用跟踪服务图计算。 |  |
| <input type="checkbox" unchecked id="switch_1190"> | `use-heap-profiling-proto-writer` | `kUseHeapProfilingProtoWriter` |  |  |

## Services Service Manager Cpp Service Executable Switches.cc (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1191"> | `service-name` | `kServiceName` | 指示要运行的服务名称。对调试很有用，或者如果服务可执行文件构建为支持作为多个潜在不同服务运行。 |  |
| <input type="checkbox" unchecked id="switch_1192"> | `service-request-attachment-name` | `kServiceRequestAttachmentName` | 附加到服务接收的传入Mojo邀请的|mojo::PendingReceiver&lt;service_manager::mojom::Service&gt;|消息管道句柄的名称。 |  |

## Services Service Manager Switches.cc (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1193"> | `enable-service-manager-tracing` | `kEnableTracing` | 启用跟踪服务。 |  |

## Shell (8 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1194"> | `content-shell-hide-toolbar` | `kContentShellHideToolbar` | 从content_shell的主机窗口隐藏工具栏。 |  |
| <input type="checkbox" unchecked id="switch_1195"> | `content-shell-host-window-size` | `kContentShellHostWindowSize` | content_shell主机窗口的大小（即"800x600"）。 |  |
| <input type="checkbox" unchecked id="switch_1196"> | `disable-system-font-check` | `kDisableSystemFontCheck` | 指定时禁用系统字体检查。 |  |
| <input type="checkbox" unchecked id="switch_1197"> | `expose-internals-for-testing` | `kExposeInternalsForTesting` | 向JavaScript公开window.internals对象，用于依赖它的Web测试的交互式开发和调试。 |  |
| <input type="checkbox" unchecked id="switch_1198"> | `isolated-context-origins` | `kIsolatedContextOrigins` | 为给定的逗号分隔来源列表启用受[IsolatedContext] IDL属性保护的API。 |  |
| <input type="checkbox" unchecked id="switch_1199"> | `remote-debugging-address` | `kRemoteDebuggingAddress` | 使用给定地址而不是默认环回来接受远程调试连接。注意远程调试协议不执行任何身份验证，因此过度暴露可能存在安全风险。 |  |
| <input type="checkbox" unchecked id="switch_1200"> | `run-web-tests` | `kRunWebTests` | 在Web测试模式下运行Content Shell，为blink Web测试注入仅测试的行为。 |  |
| <input type="checkbox" unchecked id="switch_1201"> | `test-register-standard-scheme` | `kTestRegisterStandardScheme` | 将提供的方案注册为标准方案。 |  |

## Signin (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1202"> | `clear-token-service` | `kClearTokenService` | 在使用令牌服务之前清除它。这允许在测试期间模拟凭据过期。 |  |

## Skia (2 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1203"> | `text-contrast` | `kTextContrast` | 文本对比度调整。 |  |
| <input type="checkbox" unchecked id="switch_1204"> | `text-gamma` | `kTextGamma` | 文本伽马值调整。 |  |

## Switches.cc (22 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1205"> | `background-thread-pool-field-trial` | `kBackgroundThreadPoolFieldTrial` | 配置后台线程池字段试验。 |  |
| <input type="checkbox" unchecked id="switch_1206"> | `disable-best-effort-tasks` | `kDisableBestEffortTasks` | 延迟TaskPriority::BEST_EFFORT任务的执行直到关闭。 |  |
| <input type="checkbox" unchecked id="switch_1207"> | `disable-breakpad` | `kDisableBreakpad` | 禁用崩溃报告。 |  |
| <input type="checkbox" unchecked id="switch_1208"> | `disable-features` | `kDisableFeatures` | 要禁用的功能名称的逗号分隔列表。另请参见kEnableFeatures。 |  |
| <input type="checkbox" unchecked id="switch_1209"> | `disable-low-end-device-mode` | `kDisableLowEndDeviceMode` | 设置时强制禁用低端设备模式。 |  |
| <input type="checkbox" unchecked id="switch_1210"> | `enable-features` | `kEnableFeatures` | 要启用的功能名称的逗号分隔列表。另请参见kDisableFeatures。 |  |
| <input type="checkbox" unchecked id="switch_1211"> | `enable-low-end-device-mode` | `kEnableLowEndDeviceMode` | 设置时强制低端设备模式。 |  |
| <input type="checkbox" unchecked id="switch_1212"> | `field-trial-handle` | `kFieldTrialHandle` | 包含要在进程间共享的字段试验状态的共享内存段的句柄。此开关的参数由逗号分隔的段组成：- 共享内存的平台特定句柄ID作为字符串。- （仅Windows）i=通过复制继承或p=子进程必须打开父进程。- 共享内存块GUID的高64位。- 共享内存块GUID的低64位。- 共享内存段的大小作为字符串。 |  |
| <input type="checkbox" unchecked id="switch_1213"> | `force-fieldtrials` | `kForceFieldTrials` | 此选项可用于在本地测试更改时强制字段试验。参数是名称和值对的列表，用斜杠分隔。如果试验名称以星号为前缀，该试验将开始激活。例如，以下参数定义了两个试验，第二个被激活："GoogleNow/Enable/*MaterialDesignNTP/Default/"。此选项也可用于浏览器进程使用相同格式将试验列表发送到非浏览器进程。详见field_trial.h中的FieldTrialList::CreateTrialsFromString()。 |  |
| <input type="checkbox" unchecked id="switch_1214"> | `full-memory-crash-report` | `kFullMemoryCrashReport` | 生成完整内存崩溃转储。 |  |
| <input type="checkbox" unchecked id="switch_1215"> | `log-best-effort-tasks` | `kLogBestEffortTasks` | 记录所有以TaskPriority::BEST_EFFORT发布的任务的信息。使用此选项诊断被认为由TaskPriority::BEST_EFFORT执行围栅引起的问题。注意：发布到非BEST_EFFORT UpdateableSequencedTaskRunner且优先级后来降低到BEST_EFFORT的任务不会被记录。 |  |
| <input type="checkbox" unchecked id="switch_1216"> | `metrics-shmem-handle` | `kMetricsSharedMemoryHandle` | 子进程应用于将直方图传回浏览器进程的共享内存段的句柄。 |  |
| <input type="checkbox" unchecked id="switch_1217"> | `noerrdialogs` | `kNoErrorDialogs` | 存在时抑制所有错误对话框。 |  |
| <input type="checkbox" unchecked id="switch_1218"> | `profiling-at-start` | `kProfilingAtStart` | 在启动时为浏览器进程启动基于采样的分析器。这仅在使用gn arg enable_profiling = true构建Chrome时才有效。输出将发送到kProfilingFile的值。 |  |
| <input type="checkbox" unchecked id="switch_1219"> | `profiling-file` | `kProfilingFile` | 指定分析输出的位置。这仅在使用gyp变量profiling=1或gn arg enable_profiling=true构建Chrome时才有效。如果存在{pid}将被进程的pid替换。如果存在{count}将在为此进程生成配置文件时递增。默认情况下浏览器为chrome-profile-{pid}，测试为test-profile-{pid}。 |  |
| <input type="checkbox" unchecked id="switch_1220"> | `profiling-flush` | `kProfilingFlush` | 控制配置文件数据是否定期刷新到文件。通常数据在退出时写入，但存在chromium不干净退出的情况（特别是使用单进程时）。可以指定以秒为单位的时间。 |  |
| <input type="checkbox" unchecked id="switch_1221"> | `test-child-process` | `kTestChildProcess` | 运行生成子进程的某些测试时，此开关向测试框架指示当前进程是子进程。 |  |
| <input type="checkbox" unchecked id="switch_1222"> | `trace-to-file` | `kTraceToFile` | 将来自这些类别的跟踪事件发送到文件。--trace-to-file本身发送到默认类别。 |  |
| <input type="checkbox" unchecked id="switch_1223"> | `trace-to-file-name` | `kTraceToFileName` | 指定--trace-to-file的文件名。如果未指定，将使用默认文件名。 |  |
| <input type="checkbox" unchecked id="switch_1224"> | `v` | `kV` | 给出默认最大活动V日志记录级别；0是默认值。通常正值用于V日志记录级别。 |  |
| <input type="checkbox" unchecked id="switch_1225"> | `vmodule` | `kVModule` | 给出每个模块的最大V日志记录级别以覆盖--v给出的值。例如"my_module=2,foo=3"将更改源文件"my_module."和"foo."中所有代码的日志记录级别（此匹配也忽略"-inl"后缀）。包含正斜杠或反斜杠的任何模式将针对整个路径名而不仅仅是模块进行测试。例如，"/foo/bar/=2"将更改"foo/bar"目录下源文件中所有代码的日志记录级别。 |  |
| <input type="checkbox" unchecked id="switch_1226"> | `wait-for-debugger` | `kWaitForDebugger` | 将等待60秒让调试器附加到进程。 |  |

## Sync (13 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1227"> | `cryptauth-http-host` | `kCryptAuthHTTPHost` | 覆盖CryptAuth使用的默认Google API URL (https://www.googleapis.com)。 |  |
| <input type="checkbox" unchecked id="switch_1228"> | `cryptauth-v2-devicesync-http-host` | `kCryptAuthV2DeviceSyncHTTPHost` | 覆盖CryptAuth v2 DeviceSync的默认URL：https://cryptauthdevicesync.googleapis.com。 |  |
| <input type="checkbox" unchecked id="switch_1229"> | `cryptauth-v2-enrollment-http-host` | `kCryptAuthV2EnrollmentHTTPHost` | 覆盖CryptAuth v2 Enrollment的默认URL：https://cryptauthenrollment.googleapis.com。 |  |
| <input type="checkbox" unchecked id="switch_1230"> | `disable-sync` | `kDisableSync` | 禁用将浏览器数据同步到Google帐户。 |  |
| <input type="checkbox" unchecked id="switch_1231"> | `disable-sync-invalidation-optimizations` | `kDisableSyncInvalidationOptimizations` | 禁用同步失效Commit请求中的优化标志。这对实时测试避免不稳定性很有用。 |  |
| <input type="checkbox" unchecked id="switch_1232"> | `enable-local-sync-backend` | `kEnableLocalSyncBackend` | 启用由LoopbackServer实现的本地同步后端。 |  |
| <input type="checkbox" unchecked id="switch_1233"> | `local-sync-backend-dir` | `kLocalSyncBackendDir` | 指定本地同步后端目录。名称选择模仿user-data-dir等。此标志仅在enable-local-sync-backend标志存在时才有意义。 |  |
| <input type="checkbox" unchecked id="switch_1234"> | `sync-deferred-startup-timeout-seconds` | `kSyncDeferredStartupTimeoutSeconds` | 允许覆盖延迟初始化回退超时。 |  |
| <input type="checkbox" unchecked id="switch_1235"> | `sync-include-specifics` | `kSyncIncludeSpecificsInProtocolLog` | 控制chrome://sync-internals上"Capture Specifics"标志的初始状态是否启用。 |  |
| <input type="checkbox" unchecked id="switch_1236"> | `sync-protocol-log-buffer-size` | `kSyncProtocolLogBufferSize` | 控制缓冲的ProtocolEvents数量，因此可以在新打开的chrome://sync-internals标签页上显示。 |  |
| <input type="checkbox" unchecked id="switch_1237"> | `sync-short-initial-retry-override` | `kSyncShortInitialRetryOverride` | 此标志使同步在遇到错误时非常快速地重试（见polling_constants.h），作为指数退避的第一步。 |  |
| <input type="checkbox" unchecked id="switch_1238"> | `sync-short-nudge-delay-for-test` | `kSyncShortNudgeDelayForTest` | 此标志显著缩短nudge周期之间的延迟。其主要目的是加速集成测试。正常延迟允许合并和防止服务器过载，所以除非您真的确定这是您想要的，否则不要使用此选项。 |  |
| <input type="checkbox" unchecked id="switch_1239"> | `sync-url` | `kSyncServiceURL` | 覆盖用于配置文件同步的默认服务器。 |  |

## Test (53 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1240"> | `allow-external-pages` | `kAllowExternalPages` | 允许在Web测试期间访问外部页面。 |  |
| <input type="checkbox" unchecked id="switch_1241"> | `also-emit-success-logs` | `kAlsoEmitSuccessLogs` | 同时为成功的测试发出完整的事件跟踪日志。 |  |
| <input type="checkbox" unchecked id="switch_1242"> | `always-use-complex-text` | `kAlwaysUseComplexText` | 始终对Web测试使用复杂文本路径。 |  |
| <input type="checkbox" unchecked id="switch_1243"> | `crash-on-failure` | `kCrashOnFailure` | 当指定给"enable-leak-detection"命令行选项时，使泄露检测器在发现泄露时立即崩溃。 |  |
| <input type="checkbox" unchecked id="switch_1244"> | `debug-devtools` | `kDebugDevTools` | 在调试模式下运行开发者工具测试（非捆绑和最小化）。 |  |
| <input type="checkbox" unchecked id="switch_1245"> | `devtools-code-coverage` | `kDevtoolsCodeCoverage` | 输出JavaScript代码覆盖率的目录。提供时在选定的浏览器测试中启用覆盖。 |  |
| <input type="checkbox" unchecked id="switch_1246"> | `disable-auto-wpt-origin-isolation` | `kDisableAutoWPTOriginIsolation` | 禁用Web平台测试域的自动源隔离。我们通常将它们源隔离以获得更好的测试覆盖，但选择加入源隔离的测试需要禁用此功能。 |  |
| <input type="checkbox" unchecked id="switch_1247"> | `disable-headless-mode` | `kDisableHeadlessMode` | Disables the shell from beginning in headless mode. Tests will then attempt to use the hardware GPU for rendering. This is only followed when kRunWebTests is set. |  |
| <input type="checkbox" unchecked id="switch_1248"> | `enable-accelerated-2d-canvas` | `kEnableAccelerated2DCanvas` | 启用加速2D画布。 |  |
| <input type="checkbox" unchecked id="switch_1249"> | `enable-font-antialiasing` | `kEnableFontAntialiasing` | 为像素测试启用字体抗锯齿。 |  |
| <input type="checkbox" unchecked id="switch_1250"> | `enable-leak-detection` | `kEnableLeakDetection` | 启用加载网页的泄露检测。这允许我们检查重新加载网页是否正确释放了与Web相关的对象。 |  |
| <input type="checkbox" unchecked id="switch_1251"> | `encode-binary` | `kEncodeBinary` | 使用base64编码二进制Web测试结果（图像、音频）。 |  |
| <input type="checkbox" unchecked id="switch_1252"> | `enforce-exact-positive-filter` | `kEnforceExactPositiveFilter` | 强制以完整名称（不使用通配符）运行正面过滤器文件中列出的测试用例。如果设置，只允许过滤器文件中的确切正面过滤器。传递--gtest_filter、正面通配符过滤器或负面过滤器将使测试启动器失败。如果任何测试用例在源文件中被禁用或删除，测试套件将失败。 |  |
| <input type="checkbox" unchecked id="switch_1253"> | `fuzz` | `kFuzz` | 以下三个开关与fuzztest中的匹配，并以相同方式定义。我们在此测试套件中了解它们，以便在模糊测试模式下采取不同行为。这些似乎是非常稳定的fuzztest标志，我们不太可能需要以类似方式检测其他标志，但如果这被证明不稳定，我们可以添加上游fuzztest API，如fuzztest::AreWeFuzzing，并使用它而不是检测任何标志。 |  |
| <input type="checkbox" unchecked id="switch_1254"> | `fuzz_for` | `kFuzzFor` | 模糊测试持续时间。 |  |
| <input type="checkbox" unchecked id="switch_1255"> | `help` | `kHelpFlag` | 显示帮助消息的标志。 |  |
| <input type="checkbox" unchecked id="switch_1256"> | `initialize-mojo-as-broker` | `kInitializeMojoAsBroker` | 将Mojo初始化为代理。 |  |
| <input type="checkbox" unchecked id="switch_1257"> | `inspector-protocol-log` | `kInspectorProtocolLog` | 指定包含Chrome开发者工具协议日志的文件路径。日志文件中的每行都应该是JSON格式的协议消息。测试运行器将使用此日志文件为运行的任何inspector-protocol测试编写后端脚本。通常您会希望使用日志运行单个测试以重现超时或崩溃。 |  |
| <input type="checkbox" unchecked id="switch_1258"> | `isolated-script-test-launcher-retry-limit` | `kIsolatedScriptTestLauncherRetryLimit` | 独立脚本测试启动器重试限制。 |  |
| <input type="checkbox" unchecked id="switch_1259"> | `list_fuzz_tests` | `kListFuzzTests` | 列出模糊测试。 |  |
| <input type="checkbox" unchecked id="switch_1260"> | `mojo-is-broker` | `kMojoIsBroker` | 强制进程的全局Mojo节点配置为代理。仅对使用MojoTestSuiteBase的测试运行器有效。 |  |
| <input type="checkbox" unchecked id="switch_1261"> | `no-mojo` | `kNoMojo` | 在进程中完全禁用Mojo初始化。仅适用于测试子进程。请参见base::MultiprocessTest。 |  |
| <input type="checkbox" unchecked id="switch_1262"> | `perf-test-print-uma-means` | `kPerfTestPrintUmaMeans` | 显示本机性能测试正在监控的直方图的均值。请注意，这仅适用于PerformanceTest子类。 |  |
| <input type="checkbox" unchecked id="switch_1263"> | `rebaseline-pixel-tests` | `kRebaselinePixelTests` | 如果输出和参考不匹配，使像素测试覆盖其参考。 |  |
| <input type="checkbox" unchecked id="switch_1264"> | `reset-browsing-instance-between-tests` | `kResetBrowsingInstanceBetweenTests` | 强制每个Web测试在新的BrowsingInstance中运行。对于BrowsingInstance保留来自源隔离请求状态的源隔离Web测试是必需的，但此标志可能对其他Web测试有益。 |  |
| <input type="checkbox" unchecked id="switch_1265"> | `single-process-tests` | `kSingleProcessTests` | 在单个进程中运行所有测试和启动器的标志。对于在调试器中调试特定测试很有用。 |  |
| <input type="checkbox" unchecked id="switch_1266"> | `stable-release-mode` | `kStableReleaseMode` | 这使我们禁用一些Web平台运行时功能，以便我们像测试稳定版本一样测试content_shell。只有在设置kRunWebTest时才遵循。有关功能级别，请参见third_party/blink/renderer/platform/RuntimeEnabledFeatures.md。 |  |
| <input type="checkbox" unchecked id="switch_1267"> | `test-launcher-batch-limit` | `kTestLauncherBatchLimit` | 单批次运行的最大测试数。 |  |
| <input type="checkbox" unchecked id="switch_1268"> | `test-launcher-bot-mode` | `kTestLauncherBotMode` | 为持续集成机器人设置理想的默认值，例如并行测试执行和测试重试。 |  |
| <input type="checkbox" unchecked id="switch_1269"> | `test-launcher-debug-launcher` | `kTestLauncherDebugLauncher` | 使调试启动器本身成为可能。默认情况下，启动器在检测到调试器存在时会自动切换到单进程模式。 |  |
| <input type="checkbox" unchecked id="switch_1270"> | `test-launcher-filter-file` | `kTestLauncherFilterFile` | 包含测试过滤器的文件路径列表（用';'分隔）（每行一个模式）。 |  |
| <input type="checkbox" unchecked id="switch_1271"> | `test-launcher-force-run-broken-tests` | `kTestLauncherForceRunBrokenTests` | 即使发生太多测试错误，也强制运行所有请求的测试和重试。 |  |
| <input type="checkbox" unchecked id="switch_1272"> | `test-launcher-interactive` | `kTestLauncherInteractive` | 测试启动器是否应在"交互模式"下启动，这会禁用超时（对特定测试类型可能有其他影响）。 |  |
| <input type="checkbox" unchecked id="switch_1273"> | `test-launcher-jobs` | `kTestLauncherJobs` | 并行测试启动器作业数。 |  |
| <input type="checkbox" unchecked id="switch_1274"> | `test-launcher-list-tests` | `kTestLauncherListTests` | 编译测试列表的路径。 |  |
| <input type="checkbox" unchecked id="switch_1275"> | `test-launcher-output` | `kTestLauncherOutput` | 自定义测试启动器格式的测试结果文件路径。 |  |
| <input type="checkbox" unchecked id="switch_1276"> | `test-launcher-output-bytes-limit` | `kTestLauncherOutputBytesLimit` | 单个测试允许的最大输出字节数。超过此限制会导致截断输出并使测试失败。 |  |
| <input type="checkbox" unchecked id="switch_1277"> | `test-launcher-print-temp-leaks` | `kTestLauncherPrintTempLeaks` | 使测试启动器打印关于子进程临时目录中泄漏文件和/或目录的信息。 |  |
| <input type="checkbox" unchecked id="switch_1278"> | `test-launcher-print-test-stdio` | `kTestLauncherPrintTestStdio` | 控制何时将测试stdio显示为启动器标准输出一部分的标志。 |  |
| <input type="checkbox" unchecked id="switch_1279"> | `test-launcher-print-timestamps` | `kTestLauncherPrintTimestamps` | 在测试启动器中打印时间戳。这对调试测试缓慢很有帮助。目前它打印以下日志：* 每个测试结束时的时间。* 等待测试运行时的时间。使用此标志可以帮助您回答"运行前10000个测试花了多长时间"等问题。请仅在构建器上临时保留此标志，因为这些日志有点垃圾信息。 |  |
| <input type="checkbox" unchecked id="switch_1280"> | `test-launcher-print-writable-path` | `kTestLauncherPrintWritablePath` | 打印可写路径并退出（供内部使用）。 |  |
| <input type="checkbox" unchecked id="switch_1281"> | `test-launcher-retries-left` | `kTestLauncherRetriesLeft` | 指示剩余多少重试。测试通常不应传入此标志。此标志用于启动器向运行器进程传递剩余重试信息。 |  |
| <input type="checkbox" unchecked id="switch_1282"> | `test-launcher-retry-limit` | `kTestLauncherRetryLimit` | 这两个标志具有相同的效果，但不要同时使用它们。将来更推荐isolated-script-test-launcher-retry-limit。失败后重试测试的最大次数。 |  |
| <input type="checkbox" unchecked id="switch_1283"> | `test-launcher-shard-index` | `kTestLauncherShardIndex` | 要运行的测试分片索引，从0（第一个分片）到总分片数减一（最后一个分片）。 |  |
| <input type="checkbox" unchecked id="switch_1284"> | `test-launcher-summary-output` | `kTestLauncherSummaryOutput` | 包含测试启动器所有信息的测试结果文件路径。 |  |
| <input type="checkbox" unchecked id="switch_1285"> | `test-launcher-test-part-results-limit` | `kTestLauncherTestPartResultsLimit` | 输出中测试部分结果的限制。默认限制是10。负值将完全禁用限制。 |  |
| <input type="checkbox" unchecked id="switch_1286"> | `test-launcher-timeout` | `kTestLauncherTimeout` | 测试应在超时前等待的时间（以毫秒为单位）。 |  |
| <input type="checkbox" unchecked id="switch_1287"> | `test-launcher-total-shards` | `kTestLauncherTotalShards` | 分片总数。所有分片必须相同。 |  |
| <input type="checkbox" unchecked id="switch_1288"> | `test-launcher-trace` | `kTestLauncherTrace` | 保存测试启动器执行跟踪的路径。 |  |
| <input type="checkbox" unchecked id="switch_1289"> | `test-tiny-timeout` | `kTestTinyTimeout` | TODO(phajdan.jr): 清理开关名称。 |  |
| <input type="checkbox" unchecked id="switch_1290"> | `ui-test-action-max-timeout` | `kUiTestActionMaxTimeout` | UI测试操作最大超时。 |  |
| <input type="checkbox" unchecked id="switch_1291"> | `ui-test-action-timeout` | `kUiTestActionTimeout` | UI测试操作超时。 |  |
| <input type="checkbox" unchecked id="switch_1292"> | `with-death-test-stack-traces` | `kWithDeathTestStackTraces` | 不在死亡测试中抑制堆栈跟踪。 |  |

## Third Party Blink Switches.cc (35 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1293"> | `allow-pre-commit-input` | `kAllowPreCommitInput` | 允许在提交帧之前处理输入。TODO(crbug.com/987626): 由headless使用。寻找不涉及命令行开关的方法。 |  |
| <input type="checkbox" unchecked id="switch_1294"> | `blink-settings` | `kBlinkSettings` | 设置blink设置。格式为<name>[=<value>],<name>[=<value>],...。名称在Settings.json5中声明。对于布尔类型，使用"true"、"false"，或省略'=<value>'部分设置为true。对于枚举类型，使用枚举值的整数值。在其他命令行标志和首选项之后应用。 |  |
| <input type="checkbox" unchecked id="switch_1295"> | `character` | `kTouchTextSelectionStrategy_Character` | 字符触摸文本选择策略。 |  |
| <input type="checkbox" unchecked id="switch_1296"> | `dark-mode-settings` | `kDarkModeSettings` | 设置深色模式设置。格式为[<param>=<value>],[<param>=<value>],...。参数接受整数或浮点值。如果未指定参数，则使用默认深色模式设置。有效参数如下。"InversionAlgorithm"接受DarkModeInversionAlgorithm枚举的整数值。"ImagePolicy"接受DarkModeImagePolicy枚举的整数值。"ForegroundBrightnessThreshold"接受0到255的整数值。"BackgroundBrightnessThreshold"接受0到255的整数值。"ContrastPercent"接受-1.0到1.0的浮点值。值越高，对比度越大。 |  |
| <input type="checkbox" unchecked id="switch_1297"> | `data-url-in-svg-use-enabled` | `kDataUrlInSvgUseEnabled` | 通过企业政策覆盖SVGUseElement中data: URL的弃用。 |  |
| <input type="checkbox" unchecked id="switch_1298"> | `default-tile-height` | `kDefaultTileHeight` | 默认瓦片高度。 |  |
| <input type="checkbox" unchecked id="switch_1299"> | `default-tile-width` | `kDefaultTileWidth` | 设置合成层使用的瓦片大小。 |  |
| <input type="checkbox" unchecked id="switch_1300"> | `direction` | `kTouchTextSelectionStrategy_Direction` | 方向触摸文本选择策略。 |  |
| <input type="checkbox" unchecked id="switch_1301"> | `disable-blob-url-partitioning` | `kDisableBlobUrlPartitioning` | 通过企业政策切换Blob URL分区。 |  |
| <input type="checkbox" unchecked id="switch_1302"> | `disable-image-animation-resync` | `kDisableImageAnimationResync` | 禁止图像动画重置到开头以避免跳过许多帧。仅在启用合成器图像动画时有效。 |  |
| <input type="checkbox" unchecked id="switch_1303"> | `disable-partial-raster` | `kDisablePartialRaster` | 在渲染器中禁用部分光栅化。禁用此开关还会禁用持久GPU内存缓冲区的使用。 |  |
| <input type="checkbox" unchecked id="switch_1304"> | `disable-prefer-compositing-to-lcd-text` | `kDisablePreferCompositingToLCDText` | 当会阻止LCD文本时禁用合成层的创建。 |  |
| <input type="checkbox" unchecked id="switch_1305"> | `disable-reduce-accept-language` | `kDisableReduceAcceptLanguage` | ReduceAcceptLanguage的覆盖机制。此功能通常由基本功能控制，但需要企业政策覆盖。 |  |
| <input type="checkbox" unchecked id="switch_1306"> | `disable-rgba-4444-textures` | `kDisableRGBA4444Textures` | 禁用RGBA_4444纹理。 |  |
| <input type="checkbox" unchecked id="switch_1307"> | `disable-standardized-browser-zoom` | `kDisableStandardizedBrowserZoom` | Override mechanism for preserving the old non-standard behavior of CSS zoom. |  |
| <input type="checkbox" unchecked id="switch_1308"> | `disable-zero-copy` | `kDisableZeroCopy` | 禁用直接写入与瓦片相关的GPU内存的光栅化器。 |  |
| <input type="checkbox" unchecked id="switch_1309"> | `dump-blink-runtime-call-stats` | `kDumpRuntimeCallStats` | Logs Runtime Call Stats. --single-process also needs to be used along with this for the stats to be logged. |  |
| <input type="checkbox" unchecked id="switch_1310"> | `enable-gpu-memory-buffer-compositor-resources` | `kEnableGpuMemoryBufferCompositorResources` | 指定所有合成器资源都应由GPU内存缓冲区支持。 |  |
| <input type="checkbox" unchecked id="switch_1311"> | `enable-leak-detection-heap-snapshot` | `kEnableLeakDetectionHeapSnapshot` | 在使用内存泄漏检测时启用获取堆快照并将其转储到文件。 |  |
| <input type="checkbox" unchecked id="switch_1312"> | `enable-prefer-compositing-to-lcd-text` | `kEnablePreferCompositingToLCDText` | 在可能阻止LCD文本时启用合成层的创建。 |  |
| <input type="checkbox" unchecked id="switch_1313"> | `enable-raster-side-dark-mode-for-images` | `kEnableRasterSideDarkModeForImages` | 为图像启用光栅端深色模式。 |  |
| <input type="checkbox" unchecked id="switch_1314"> | `enable-rgba-4444-textures` | `kEnableRGBA4444Textures` | Enables RGBA_4444 textures. |  |
| <input type="checkbox" unchecked id="switch_1315"> | `enable-zero-copy` | `kEnableZeroCopy` | 启用直接写入与瓦片相关的GPU内存的光栅化器。 |  |
| <input type="checkbox" unchecked id="switch_1316"> | `force-gpu-mem-available-mb` | `kForceGpuMemAvailableMb` | 设置在cc中可能为GPU资源分配的内存总量。 |  |
| <input type="checkbox" unchecked id="switch_1317"> | `gpu-rasterization-msaa-sample-count` | `kGpuRasterizationMSAASampleCount` | The number of multisample antialiasing samples for GPU rasterization. Requires MSAA support on GPU to have an effect. 0 disables MSAA. |  |
| <input type="checkbox" unchecked id="switch_1318"> | `js-flags` | `kJavaScriptFlags` | 指定传递给JS引擎的标志。 |  |
| <input type="checkbox" unchecked id="switch_1319"> | `max-untiled-layer-height` | `kMaxUntiledLayerHeight` | 设置合成层开始分块的宽度和高度。 |  |
| <input type="checkbox" unchecked id="switch_1320"> | `max-untiled-layer-width` | `kMaxUntiledLayerWidth` |  |  |
| <input type="checkbox" unchecked id="switch_1321"> | `min-height-for-gpu-raster-tile` | `kMinHeightForGpuRasterTile` | 设置GPU光栅的最小瓦片高度。 |  |
| <input type="checkbox" unchecked id="switch_1322"> | `network-quiet-timeout` | `kNetworkQuietTimeout` | Sets the timeout seconds of the network-quiet timers in IdlenessDetector. Used by embedders who want to change the timeout time in order to run web contents on various embedded devices and changeable network bandwidths in different regions. For example, it&#x27;s useful when using FirstMeaningfulPaint signal to dismiss a splash screen. |  |
| <input type="checkbox" unchecked id="switch_1323"> | `shared-array-buffer-allowed-origins` | `kSharedArrayBufferAllowedOrigins` | Comma-separated list of origins that can use SharedArrayBuffer without enabling cross-origin isolation. |  |
| <input type="checkbox" unchecked id="switch_1324"> | `show-layout-shift-regions` | `kShowLayoutShiftRegions` | 在网页中可视化渲染布局偏移矩形周围的边框，以帮助调试和研究布局偏移。 |  |
| <input type="checkbox" unchecked id="switch_1325"> | `show-paint-rects` | `kShowPaintRects` | 在网页中可视化渲染绘制矩形周围的边框，以帮助调试和研究绘制行为。 |  |
| <input type="checkbox" unchecked id="switch_1326"> | `touch-selection-strategy` | `kTouchTextSelectionStrategy` | Controls how text selection granularity changes when touch text selection handles are dragged. Should be &quot;character&quot; or &quot;direction&quot;. If not specified, the platform default is used. |  |
| <input type="checkbox" unchecked id="switch_1327"> | `web-audio-bypass-output-buffering-opt-out` | `kWebAudioBypassOutputBufferingOptOut` | Used to communicate managed policy for WebAudioBypassOutputBuffering.  This feature is typically controlled by a RuntimeEnabledFeature, but requires an enterprise policy override. |  |

## Third Party Blink Switches.h (5 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1328"> | `0` | `kIntensiveWakeUpThrottlingPolicy_ForceDisable` | 强制禁用密集唤醒节流策略。 |  |
| <input type="checkbox" unchecked id="switch_1329"> | `1` | `kIntensiveWakeUpThrottlingPolicy_ForceEnable` | 强制启用密集唤醒节流策略。 |  |
| <input type="checkbox" unchecked id="switch_1330"> | `css-custom-state-deprecated-syntax-enabled` | `kCSSCustomStateDeprecatedSyntaxEnabled` | 启用CSS自定义状态已弃用语法。 |  |
| <input type="checkbox" unchecked id="switch_1331"> | `intensive-wake-up-throttling-policy` | `kIntensiveWakeUpThrottlingPolicy` | 密集唤醒节流策略。 |  |
| <input type="checkbox" unchecked id="switch_1332"> | `legacy-tech-report-policy-enabled` | `kLegacyTechReportPolicyEnabled` | 启用传统技术报告策略。 |  |

## Tracing (19 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1333"> | `background-tracing-output-path` | `kBackgroundTracingOutputPath` | 为跟踪数据设置本地文件夹目标。仅在也指定kEnableBackgroundTracing时使用。 |  |
| <input type="checkbox" unchecked id="switch_1334"> | `default-trace-buffer-size-limit-in-kb` | `kDefaultTraceBufferSizeLimitInKb` | 仅在我们未在跟踪配置中设置缓冲区大小时使用，并将用于所有跟踪会话。如果未提供，我们将使用perfetto_config.cc中提供的默认值。 |  |
| <input type="checkbox" unchecked id="switch_1335"> | `enable-background-tracing` | `kEnableBackgroundTracing` | 通过将场景配置作为参数传递来启用后台跟踪。配置是在third_party/perfetto/protos/perfetto/config/chrome/scenario_config.proto中定义的序列化proto perfetto.protos.ChromeFieldTracingConfig。可以使用protoc生成序列化proto配置：protoc --encode=perfetto.protos.ChromeFieldTracingConfig --proto_path=third_party/perfetto/ third_party/perfetto/protos/perfetto/config/chrome/scenario_config.proto < {input txt config}.pbtxt > {output proto config}.pb |  |
| <input type="checkbox" unchecked id="switch_1336"> | `enable-tracing` | `kEnableTracing` | 启用跟踪。 |  |
| <input type="checkbox" unchecked id="switch_1337"> | `enable-tracing-format` | `kEnableTracingFormat` | 启用跟踪格式。 |  |
| <input type="checkbox" unchecked id="switch_1338"> | `enable-tracing-output` | `kEnableTracingOutput` | 与上面的标志类似，具有以下差异：- 将生成更详细的基名。- 如果值为空或以路径分隔符结尾，将使用提供的目录（空代表当前目录）并生成详细的基名文件。如果指定了--trace-startup-file，则忽略此项。 |  |
| <input type="checkbox" unchecked id="switch_1339"> | `perfetto-disable-interning` | `kPerfettoDisableInterning` | 在perfetto proto格式中为每个TraceEvent重复可内部化的数据。 |  |
| <input type="checkbox" unchecked id="switch_1340"> | `trace-buffer-handle` | `kTraceBufferHandle` | 子进程应用于将跟踪数据传输回跟踪服务的共享内存段的句柄。此标志允许在沙箱设置之前记录跟踪。 |  |
| <input type="checkbox" unchecked id="switch_1341"> | `trace-config-file` | `kTraceConfigFile` | 通过传递包含chrome Json跟踪配置的文件路径作为参数来启用启动跟踪。如果提供了--trace-startup或--trace-shutdown，此标志将被忽略。 |  |
| <input type="checkbox" unchecked id="switch_1342"> | `trace-config-handle` | `kTraceConfigHandle` | 导致从启动时记录TRACE_EVENT标志，传递包含序列化perfetto配置的SMB句柄。如果提供了--trace-startup或--trace-shutdown，此标志将被忽略。 |  |
| <input type="checkbox" unchecked id="switch_1343"> | `trace-perfetto-config-file` | `kTracePerfettoConfigFile` | 通过传递包含perfetto配置的文件路径作为参数来启用启动跟踪。配置是在third_party/perfetto/protos/perfetto/config/trace_config.proto中定义的序列化或base64编码proto perfetto.protos.TraceConfig。如果提供了--trace-startup或--trace-shutdown，此标志将被忽略。 |  |
| <input type="checkbox" unchecked id="switch_1344"> | `trace-smb-size` | `kTraceSmbSize` | 配置用于跟踪的共享内存缓冲区的大小。值以kB为单位提供。默认为4096。应该是SMB页面大小的倍数（目前桌面上为32kB，Android上为4kB）。 |  |
| <input type="checkbox" unchecked id="switch_1345"> | `trace-startup` | `kTraceStartup` | 导致从启动时记录TRACE_EVENT标志。可选地，可以指定要包含的特定跟踪类别（例如--trace-startup=base,net），否则记录所有事件。设置此标志会导致第一次调用BeginTracing()接收自启动以来的所有跟踪事件。历史上，--trace-startup用于浏览器启动分析，--enable-tracing用于浏览器测试跟踪。现在它们共享相同的实现，但仍支持两者以避免破坏现有工作流。它们之间唯一的区别是默认持续时间（trace-startup为5秒，enable-tracing为无限制）。如果两者都指定，'trace-startup'优先。在Chrome中，您可能会发现--trace-startup-file和--trace-startup-duration用于控制跟踪的自动保存（在仅基础的TraceLog组件中不支持）。 |  |
| <input type="checkbox" unchecked id="switch_1346"> | `trace-startup-duration` | `kTraceStartupDuration` | 设置启动跟踪结束前的时间（秒）。如果省略：- 如果指定了--trace-startup，使用默认的5秒。- 如果指定了--enable-tracing，跟踪持续到浏览器关闭。否则无效果。 |  |
| <input type="checkbox" unchecked id="switch_1347"> | `trace-startup-file` | `kTraceStartupFile` | 如果提供，设置启动跟踪将存储到的文件，如果省略，将使用默认的当前目录中的"chrometrace.log"。除非同时提供--trace-startup，否则无效果。示例：--trace-startup --trace-startup-file=/tmp/trace_event.log 作为特殊情况，可以设置为'none' - 这会禁用自动将结果保存到文件，第一次手动记录的跟踪将接收自启动以来的所有事件。 |  |
| <input type="checkbox" unchecked id="switch_1348"> | `trace-startup-format` | `kTraceStartupFormat` | 设置跟踪的输出格式，有效值为"json"和"proto"。如果未设置，当前默认为"proto"。与json不同，"proto"支持增量写入跟踪到输出文件，如果浏览器进程意外终止，更可能保留更多数据。如果"trace-startup-owner"不是"controller"，则忽略。 |  |
| <input type="checkbox" unchecked id="switch_1349"> | `trace-startup-owner` | `kTraceStartupOwner` | 指定启动跟踪会话的协调器。如果使用传统跟踪后端而不是perfetto，提供此标志不是必需的。有效值：'controller'、'devtools'或'system'。默认为'controller'。如果指定'controller'，会话通过TracingController控制和停止（例如实现超时）。如果指定'devtools'，启动跟踪会话将由DevTools拥有，因此可以通过连接到浏览器端点的第一个会话上的DevTools Tracing域来控制（即停止）。如果指定'system'，系统Perfetto服务应该已经在支持的平台上跟踪（目前仅Android）。会话通过停止系统跟踪的正常方法停止。 |  |
| <input type="checkbox" unchecked id="switch_1350"> | `trace-startup-record-mode` | `kTraceStartupRecordMode` | 如果提供，设置跟踪记录模式和选项；否则，将使用默认的"record-until-full"模式。 |  |
| <input type="checkbox" unchecked id="switch_1351"> | `trace-to-console` | `kTraceToConsole` | 向控制台发送跟踪信息的格式化版本。 |  |

## Translate (3 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1352"> | `translate-ranker-model-url` | `kTranslateRankerModelURL` | 覆盖下载翻译排名器模型的URL。 |  |
| <input type="checkbox" unchecked id="switch_1353"> | `translate-script-url` | `kTranslateScriptURL` | 覆盖用于Google翻译的默认服务器。 |  |
| <input type="checkbox" unchecked id="switch_1354"> | `translate-security-origin` | `kTranslateSecurityOrigin` | 覆盖翻译在隔离世界中运行的安全源。 |  |

## Ui Gl Gl Switches.cc (22 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1355"> | `direct-composition-video-swap-chain-format` | `kDirectCompositionVideoSwapChainFormat` | 用于覆盖直接合成SDR视频覆盖层的交换链格式。 |  |
| <input type="checkbox" unchecked id="switch_1356"> | `disable-angle-features` | `kDisableANGLEFeatures` | 如果找到，禁用指定的逗号分隔的ANGLE功能。 |  |
| <input type="checkbox" unchecked id="switch_1357"> | `disable-direct-composition` | `kDisableDirectComposition` | 禁用DirectComposition。 |  |
| <input type="checkbox" unchecked id="switch_1358"> | `disable-gl-drawing-for-tests` | `kDisableGLDrawingForTests` | 禁用产生像素输出的GL绘图操作。使用此选项，GL输出将不正确，但测试将运行得更快。 |  |
| <input type="checkbox" unchecked id="switch_1359"> | `disable-gl-extensions` | `kDisableGLExtensions` | 如果找到，禁用指定的逗号分隔的GL扩展。 |  |
| <input type="checkbox" unchecked id="switch_1360"> | `disable-gpu-driver-bug-workarounds` | `kDisableGpuDriverBugWorkarounds` | 禁用各种GPU驱动程序错误的解决方案。 |  |
| <input type="checkbox" unchecked id="switch_1361"> | `disable-gpu-vsync` | `kDisableGpuVsync` | 停止GPU将演示与垂直同步同步。 |  |
| <input type="checkbox" unchecked id="switch_1362"> | `enable-angle-features` | `kEnableANGLEFeatures` | ANGLE功能在third_party/angle/include/platform中按后端定义。如果找到，启用指定的逗号分隔的ANGLE功能。 |  |
| <input type="checkbox" unchecked id="switch_1363"> | `enable-direct-composition-video-overlays` | `kEnableDirectCompositionVideoOverlays` | 即使硬件不支持，也启用DirectComposition视频覆盖层。 |  |
| <input type="checkbox" unchecked id="switch_1364"> | `enable-gpu-service-tracing` | `kEnableGPUServiceTracing` | 启用对每个GL调用调用TRACE。 |  |
| <input type="checkbox" unchecked id="switch_1365"> | `enable-sgi-video-sync` | `kEnableSgiVideoSync` | 启用SGI_video_sync扩展的使用，该扩展可能存在驱动程序/沙箱/窗口管理器兼容性问题。 |  |
| <input type="checkbox" unchecked id="switch_1366"> | `enable-swap-buffers-with-bounds` | `kEnableSwapBuffersWithBounds` | 如果支持，启用SwapBuffersWithBounds。 |  |
| <input type="checkbox" unchecked id="switch_1367"> | `enable-unsafe-swiftshader` | `kEnableUnsafeSwiftShader` | 允许SwiftShader用于WebGL。 |  |
| <input type="checkbox" unchecked id="switch_1368"> | `gpu-no-context-lost` | `kGpuNoContextLost` | 通知Chrome在省电模式、屏保模式等情况下不会丢失GPU上下文。请注意，此标志不能确保在任何情况下都不会丢失GPU上下文，比如GPU重置。 |  |
| <input type="checkbox" unchecked id="switch_1369"> | `override-use-software-gl-for-tests` | `kOverrideUseSoftwareGLForTests` | 强制测试使用软件GL而不是硬件GPU。 |  |
| <input type="checkbox" unchecked id="switch_1370"> | `test-gl-lib` | `kTestGLLib` | 用于Linux测试的标志：对于桌面GL绑定，首先尝试加载此GL库，但如果加载失败则回退到常规库。 |  |
| <input type="checkbox" unchecked id="switch_1371"> | `tint-dc-layer` | `kTintDcLayer` | 使用以下颜色为SwapChainPresenter着色：- 解码交换链：蓝色 - VP blit：洋红色 - 带暂存纹理的VP blit：橙色 - MF代理表面：绿色。这类似于DWM中的HKLM\Software\Microsoft\Windows\DWM OverlayTestMode=1，但有助于理解SwapChainPresenter状态。 |  |
| <input type="checkbox" unchecked id="switch_1372"> | `use-adapter-luid` | `kUseAdapterLuid` | 使用具有指定LUID的适配器初始化GPU进程。这仅在Windows上使用，因为LUID是Windows特定的结构。 |  |
| <input type="checkbox" unchecked id="switch_1373"> | `use-angle` | `kUseANGLE` | 选择要使用的ANGLE后端。选项有：default：尝试多个ANGLE渲染器直到一个成功初始化，根据平台变化ES支持。d3d9：传统D3D9渲染器，仅ES2。d3d11：D3D11渲染器，ES2和ES3。warp：使用软件光栅化的D3D11渲染器，ES2和ES3。gl：桌面GL渲染器，ES2和ES3。gles：GLES渲染器，ES2和ES3。 |  |
| <input type="checkbox" unchecked id="switch_1374"> | `use-cmd-decoder` | `kUseCmdDecoder` | 使用通过命令解码器，跳过所有验证和状态跟踪。开关位于ui/gl中，因为它影响原本不会默认使用EGL绑定的平台上的GL绑定初始化。 |  |
| <input type="checkbox" unchecked id="switch_1375"> | `use-gl` | `kUseGL` | 选择GPU进程应使用的GL实现。选项有：desktop：用户安装的任何桌面OpenGL（Linux和Mac默认）。egl：用户安装的任何EGL/GLES2（Windows默认-实际上是ANGLE）。swiftshader：SwiftShader软件渲染器。 |  |
| <input type="checkbox" unchecked id="switch_1376"> | `use-gpu-in-tests` | `kUseGpuInTests` | 如果可用，在测试中使用硬件GPU。 |  |

## Ui Ui Switches.cc (13 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1377"> | `disallow-non-exact-resource-reuse` | `kDisallowNonExactResourceReuse` | 禁用重用非精确资源以满足ResourcePool请求。仅用于布局或像素测试以减少噪音。 |  |
| <input type="checkbox" unchecked id="switch_1378"> | `drm-virtual-connector-is-external` | `kDRMVirtualConnectorIsExternal` | 将DRM虚拟连接器视为外部以启用VM中的显示模式更改。 |  |
| <input type="checkbox" unchecked id="switch_1379"> | `force-caption-style` | `kForceCaptionStyle` | 强制WebVTT字幕的字幕样式。 |  |
| <input type="checkbox" unchecked id="switch_1380"> | `force-dark-mode` | `kForceDarkMode` | 在支持的平台上强制UI深色模式。 |  |
| <input type="checkbox" unchecked id="switch_1381"> | `force-high-contrast` | `kForceHighContrast` | 在本机UI绘图中强制高对比度模式，不管系统设置如何。请注意，这对Windows的影响有限：只有Aura颜色会切换到高对比度，而不是其他系统颜色。 |  |
| <input type="checkbox" unchecked id="switch_1382"> | `lang` | `kLang` | 我们想要尝试打开的语言文件。格式为language[-country]，其中language是ISO-639的2字母代码。在Linux上，此标志不起作用；请改用LC_*/LANG环境变量。 |  |
| <input type="checkbox" unchecked id="switch_1383"> | `mangle-localized-strings` | `kMangleLocalizedStrings` | 将本地化字符串转换为更长的字符串，并带有开始和结束标记，以使截断在视觉上明显。 |  |
| <input type="checkbox" unchecked id="switch_1384"> | `show-overdraw-feedback` | `kShowOverdrawFeedback` | 通过根据元素下方是否绘制了其他元素对元素进行颜色编码来可视化过度绘制。这有助于显示UI可能在何处执行不必要的渲染工作。颜色暗示屏幕上每个像素的过度绘制量，如下：真彩色：无过度绘制。蓝色：过度绘制一次。绿色：过度绘制两次。粉色：过度绘制三次。红色：过度绘制四次或更多。 |  |
| <input type="checkbox" unchecked id="switch_1385"> | `slow-down-compositing-scale-factor` | `kSlowDownCompositingScaleFactor` | 多次重新绘制所有内容以模拟更慢的机器。给出一个减速因子，使渲染器需要那么多倍的时间来完成，例如--slow-down-compositing-scale-factor=2。 |  |
| <input type="checkbox" unchecked id="switch_1386"> | `tint-composited-content` | `kTintCompositedContent` | 对合成的颜色进行着色。 |  |
| <input type="checkbox" unchecked id="switch_1387"> | `top-chrome-touch-ui` | `kTopChromeTouchUi` | 控制顶部Chrome的触摸优化UI布局。 |  |
| <input type="checkbox" unchecked id="switch_1388"> | `ui-disable-partial-swap` | `kUIDisablePartialSwap` | 禁用某些OpenGL驱动程序/模拟器所需的部分交换。 |  |
| <input type="checkbox" unchecked id="switch_1389"> | `use-system-clipboard` | `kUseSystemClipboard` | 为linux-chromeos启用ozone x11剪贴板。 |  |

## VR (3 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1390"> | `fallback` | `kWebXrHandAnonymizationStrategyFallback` | WebXR手部匿名化策略回退。 |  |
| <input type="checkbox" unchecked id="switch_1391"> | `runtime` | `kWebXrHandAnonymizationStrategyRuntime` | WebXR手部匿名化策略运行时。 |  |
| <input type="checkbox" unchecked id="switch_1392"> | `webxr-hand-anonymization-strategy` | `kWebXrHandAnonymizationStrategy` | WebXR手部匿名化策略。 |  |

## Variations (20 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1393"> | `accept-empty-variations-seed-signature` | `kAcceptEmptySeedSignatureForTesting` | 在加载变量种子时接受空签名。这是用于测试目的。 |  |
| <input type="checkbox" unchecked id="switch_1394"> | `disable-field-trial-config` | `kDisableFieldTrialTestingConfig` | 禁用fieldtrial_testing_config.json中配置的字段试验测试。 |  |
| <input type="checkbox" unchecked id="switch_1395"> | `disable-variations-safe-mode` | `kDisableVariationsSafeMode` | 禁用变量安全模式。 |  |
| <input type="checkbox" unchecked id="switch_1396"> | `disable-variations-seed-fetch` | `kDisableVariationsSeedFetch` | 禁用从服务器获取变量种子进行测试。 |  |
| <input type="checkbox" unchecked id="switch_1397"> | `disable-variations-seed-fetch-throttling` | `kDisableVariationsSeedFetchThrottling` | 在移动平台上禁用获取变量种子的节流。种子将在启动时获取，并且每次应用进入前台时获取，无论获取之间经过的时间如何。在桌面上，此开关没有效果（种子是定期获取的）。 |  |
| <input type="checkbox" unchecked id="switch_1398"> | `enable-benchmarking` | `kEnableBenchmarking` | TODO(asvitkine): 考虑删除或重命名此功能。有关更多详细信息，请参见flag_descriptions.cc。 |  |
| <input type="checkbox" unchecked id="switch_1399"> | `enable-benchmarking-api` | `kEnableBenchmarkingApi` | 启用基准测试JavaScript API。 |  |
| <input type="checkbox" unchecked id="switch_1400"> | `enable-field-trial-config` | `kEnableFieldTrialTestingConfig` | 启用fieldtrial_testing_config.json中配置的字段试验测试。如果"disable_fieldtrial_testing_config" GN标志设置为true，则此开关无效。否则，对于非Chrome品牌构建，测试配置默认已应用，除非传递了"--disable-field-trial-config"、"--force-fieldtrials"和/或"--variations-server-url"开关。但是，通过使用此开关可以应用测试配置以及指定其他字段试验（使用"--force-fieldtrials"）。对于Chrome品牌构建，测试配置默认未启用，因此需要此开关来启用它。 |  |
| <input type="checkbox" unchecked id="switch_1401"> | `enable-finch-seed-delta-compression` | `kEnableFinchSeedDeltaCompression` | 在Android上通过"首次运行"代码路径获取新种子时启用增量压缩。 |  |
| <input type="checkbox" unchecked id="switch_1402"> | `fake-variations-channel` | `kFakeVariationsChannel` | 出于变量过滤目的伪造浏览器的渠道。这仅用于测试。可能的值是"stable"、"beta"、"dev"和"canary"。这也适用于官方构建。 |  |
| <input type="checkbox" unchecked id="switch_1403"> | `force-disable-variation-ids` | `kForceDisableVariationIds` | 强制删除在X-Client-Data标头中发送的Chrome变量ID，指定为64位编码的数字实验ID列表。以字符"t"为前缀的ID将被视为触发变量ID。 |  |
| <input type="checkbox" unchecked id="switch_1404"> | `force-fieldtrial-params` | `kForceFieldTrialParams` | 此选项可用于在本地测试更改时强制字段试验的参数。参数是由关联的(trial, group)对前缀的(key, value)对的参数列表。您可以使用逗号分隔符为多个(trial, group)对指定参数列表。示例："Trial1.Group1:k1/v1/k2/v2,Trial2.Group2:k3/v3/k4/v4"。试验名称、组名称、参数名称和值都应该为所有非字母数字字符进行URL转义。 |  |
| <input type="checkbox" unchecked id="switch_1405"> | `force-variation-ids` | `kForceVariationIds` | 强制额外的Chrome变量ID将在X-Client-Data标头中发送，指定为64位编码的数字实验ID列表。以字符"t"为前缀的ID将被视为触发变量ID。 |  |
| <input type="checkbox" unchecked id="switch_1406"> | `variations-insecure-server-url` | `kVariationsInsecureServerURL` | 指定服务器用作不安全后备的自定义URL，当对|kVariationsServerURL|的请求失败时。对此URL的请求将被加密。 |  |
| <input type="checkbox" unchecked id="switch_1407"> | `variations-override-country` | `kVariationsOverrideCountry` | 允许覆盖用于评估变量的国家。这类似于chrome://translate-internals上的"覆盖变量国家"条目，但作为命令行标志公开以允许测试首次运行场景。此外，与chrome://translate-internals不同，该值不会在会话间持久保存。 |  |
| <input type="checkbox" unchecked id="switch_1408"> | `variations-seed-fetch-interval` | `kVariationsSeedFetchInterval` | 覆盖每次变量种子获取之间的时间间隔。单位为分钟。最小值为1分钟。默认值为30分钟。 |  |
| <input type="checkbox" unchecked id="switch_1409"> | `variations-seed-version` | `kVariationsSeedVersion` | 用于与子进程共享变体种子版本。 |  |
| <input type="checkbox" unchecked id="switch_1410"> | `variations-server-url` | `kVariationsServerURL` | 指定向客户端报告变量数据的服务器的自定义URL。指定此开关会在非官方构建上启用变量服务。见variations_service.cc。 |  |
| <input type="checkbox" unchecked id="switch_1411"> | `variations-state-file` | `kVariationsStateFile` | 使用值中定义的功能。使用此标志重现与实验相关的问题。从chrome://version页面复制'命令行变量'值。将其保存到文件并通过此标志传递。该值是由variations::VariationsCommandLine::WriteToString产生的base64编码JSON格式。 |  |
| <input type="checkbox" unchecked id="switch_1412"> | `variations-test-seed-path` | `kVariationsTestSeedJsonPath` | 指定用于填充本地状态种子的种子文件的位置。种子文件必须是带有键\|kVariationsCompressedSeed\|和\|kVariationsSeedSignature\|的json格式。 |  |

## Views (3 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1413"> | `disable-input-event-activation-protection` | `kDisableInputEventActivationProtectionForTesting` | 禁用对潜在意外输入事件（如在显示按钮后立即发生的按钮点击）的忽略。将此用于进行自动点击等的集成测试。 |  |
| <input type="checkbox" unchecked id="switch_1414"> | `draw-view-bounds-rects` | `kDrawViewBoundsRects` | 绘制半透明红色矩形以指示每个视图的边界。此外，当GetContentBounds()与GetLocalBounds()不同时，绘制蓝色半透明矩形。 |  |
| <input type="checkbox" unchecked id="switch_1415"> | `view-stack-traces` | `kViewStackTraces` | 在视图构造时捕获堆栈跟踪以提供更好的调试信息。 |  |

## Viz (10 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1416"> | `deadline-to-synchronize-surfaces` | `kDeadlineToSynchronizeSurfaces` | 等待激活具有依赖关系的表面的默认BeginFrames数量。 |  |
| <input type="checkbox" unchecked id="switch_1417"> | `delegated-ink-renderer` | `kDelegatedInkRenderer` | 强制使用命令行参数指定的委托墨水渲染器，而不是使用系统详细信息。可接受的值有：skia、system、none。默认为skia。 |  |
| <input type="checkbox" unchecked id="switch_1418"> | `disable-adpf` | `kDisableAdpf` | 禁用通过ADPF报告帧时间，即使设备支持。 |  |
| <input type="checkbox" unchecked id="switch_1419"> | `disable-frame-rate-limit` | `kDisableFrameRateLimit` | 在cc调度程序和显示调度程序中禁用开始帧限制。还暗示--disable-gpu-vsync（见//ui/gl/gl_switches.h）。TODO(ananta/jonross/sunnyps) http://crbug.com/346931323 一旦为Windows和其他潜在平台实现VRR支持，我们应该删除或更改此项。 |  |
| <input type="checkbox" unchecked id="switch_1420"> | `double-buffer-compositing` | `kDoubleBufferCompositing` | 将GL缓冲队列中的最大挂起帧数设置为1。 |  |
| <input type="checkbox" unchecked id="switch_1421"> | `enable-hardware-overlays` | `kEnableHardwareOverlays` | 在设备允许时启用通过硬件覆盖层合成单个元素。将标志设置为"single-fullscreen"将尝试提升单个全屏覆盖层，并在可能的情况下将其用作主帧缓冲区。 |  |
| <input type="checkbox" unchecked id="switch_1422"> | `run-all-compositor-stages-before-draw` | `kRunAllCompositorStagesBeforeDraw` | 通过等待每个阶段完成再完成帧，有效地禁用合成器帧生产阶段的管道化。 |  |
| <input type="checkbox" unchecked id="switch_1423"> | `show-aggregated-damage` | `kShowAggregatedDamage` | 在根RenderPass顶部添加DebugBorderDrawQuad，显示表面聚合后的损坏矩形。请注意，启用此功能时，在添加四边形以突出显示真实损坏矩形后，此功能会将整个输出矩形设置为已损坏，这可能隐藏损坏矩形问题。 |  |
| <input type="checkbox" unchecked id="switch_1424"> | `show-dc-layer-debug-borders` | `kShowDCLayerDebugBorders` | 显示DC层的调试边框 - 覆盖层为红色，底层为蓝色。为了清晰起见，调试边框从层矩形偏移几个像素。 |  |
| <input type="checkbox" unchecked id="switch_1425"> | `tint-composited-content-modulate` | `kTintCompositedContentModulate` | 调制调试合成器着色颜色，以便清楚地显示损坏和页面翻转更新。此功能对确定https://b.corp.google.com/issues/183260320的根本原因很有用。还必须启用着色标志"tint-composited-content"才能使用此标志。 |  |

## WebAuthn (3 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1426"> | `webauthn-gpm-pin-reset-reauth-url` | `kGpmPinResetReauthUrlSwitch` |  |  |
| <input type="checkbox" unchecked id="switch_1427"> | `webauthn-permit-enterprise-attestation` | `kPermitEnterpriseAttestationOriginList` |  |  |
| <input type="checkbox" unchecked id="switch_1428"> | `webauthn-remote-proxied-requests-allowed-additional-origin` | `kRemoteProxiedRequestsAllowedAdditionalOrigin` |  |  |

## Window Manager (1 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1429"> | `wm-window-animations-disabled` | `kWindowAnimationsDisabled` | 如果存在，则禁用动画。 |  |

## iOS (15 switches)

| Reviewed | Switch Name | Variable | Description | Review Notes |
|----------|-------------|----------|-------------|--------------|
| <input type="checkbox" unchecked id="switch_1430"> | `disable-all-injected-scripts` | `kDisableAllInjectedScripts` |  |  |
| <input type="checkbox" unchecked id="switch_1431"> | `disable-injected-feature-scripts` | `kDisableInjectedFeatureScripts` |  |  |
| <input type="checkbox" unchecked id="switch_1432"> | `disable-ios-password-suggestions` | `kDisableIOSPasswordSuggestions` | 在表单字段获得焦点时，禁用在键盘辅助视图中显示可用的密码凭据。 |  |
| <input type="checkbox" unchecked id="switch_1433"> | `disable-listed-javascript-features` | `kDisableListedJavascriptFeatures` |  |  |
| <input type="checkbox" unchecked id="switch_1434"> | `disable-listed-scripts` | `kDisableListedScripts` |  |  |
| <input type="checkbox" unchecked id="switch_1435"> | `disable-third-party-keyboard-workaround` | `kDisableThirdPartyKeyboardWorkaround` | 禁用第三方键盘地址栏变通方案。 |  |
| <input type="checkbox" unchecked id="switch_1436"> | `enable-discover-feed` | `kEnableDiscoverFeed` | 启用新标签页发现信息流。 |  |
| <input type="checkbox" unchecked id="switch_1437"> | `enable-ios-handoff-to-other-devices` | `kEnableIOSHandoffToOtherDevices` | 启用从iOS Chrome到其他Apple设备默认浏览器的接力功能支持。 |  |
| <input type="checkbox" unchecked id="switch_1438"> | `enable-listed-javascript-features` | `kEnableListedJavascriptFeatures` |  |  |
| <input type="checkbox" unchecked id="switch_1439"> | `enable-listed-scripts` | `kEnableListedScripts` |  |  |
| <input type="checkbox" unchecked id="switch_1440"> | `enable-spotlight-actions` | `kEnableSpotlightActions` | 启用Spotlight操作。 |  |
| <input type="checkbox" unchecked id="switch_1441"> | `enable-third-party-keyboard-workaround` | `kEnableThirdPartyKeyboardWorkaround` | 启用第三方键盘地址栏变通方案。 |  |
| <input type="checkbox" unchecked id="switch_1442"> | `enable-upgrade-signin-promo` | `kEnableUpgradeSigninPromo` | 启用升级登录促销。 |  |
| <input type="checkbox" unchecked id="switch_1443"> | `force-device-switcher-experience` | `kForceDeviceSwitcherExperienceCommandLineFlag` | 为参数指定的细分市场启用设备切换体验，例如"Android"。 |  |
| <input type="checkbox" unchecked id="switch_1444"> | `force-shopper-experience` | `kForceShopperExperience` | 为参数指定的细分市场启用购物功能用户体验，例如"ShoppingUser"或"Other"。 |  |

## Review Progress

### Statistics by Source
- **Accessibility**: 11 switches
- **Android Webview Aw Switches.cc**: 26 switches
- **Ash Constants Ash Switches.cc**: 251 switches
- **Ash Constants Ash Switches.h**: 1 switches
- **Assistant**: 3 switches
- **Autofill**: 7 switches
- **Borealis**: 1 switches
- **CC**: 32 switches
- **Chrome Browser Ash Android Sms Android Sms Switches.cc**: 1 switches
- **Chrome Browser Google Switches.cc**: 2 switches
- **Chrome Browser Ip Protection Ip Protection Switches.cc**: 1 switches
- **Chrome Browser Nearby Sharing Nearby Share Switches.cc**: 5 switches
- **Chrome Chrome Switches.cc**: 154 switches
- **Chrome Chrome Switches.cc, Content Content Switches.cc**: 1 switches
- **Chrome Chrome Switches.cc, Headless**: 10 switches
- **Chrome Chrome Switches.cc, Headless, Shell**: 1 switches
- **Chrome Windows Services Service Program Switches.h**: 3 switches
- **Chromecast**: 67 switches
- **Chromecast, Headless**: 1 switches
- **Chromeos Constants Chromeos Switches.cc**: 2 switches
- **Chromeos Services Machine Learning Cpp Ml Switches.cc**: 1 switches
- **Components Cast Streaming Browser Cast Streaming Switches.h**: 1 switches
- **Components Client Hints Switches.cc**: 1 switches
- **Components Component Updater Component Updater Switches.cc**: 4 switches
- **Components Dom Distiller Dom Distiller Switches.cc**: 10 switches
- **Components Dom Distiller Dom Distiller Switches.cc, VR**: 1 switches
- **Components Embedder Support Switches.cc**: 8 switches
- **Components Embedder Support Switches.cc, Graphics**: 1 switches
- **Components Embedder Support Switches.cc, Headless, iOS**: 1 switches
- **Components Error Page Error Page Switches.cc**: 2 switches
- **Components Google Google Switches.cc**: 2 switches
- **Components Heap Profiling In Process Switches.cc**: 1 switches
- **Components Media Router Providers Cast Certificate Switches.cc**: 2 switches
- **Components Network Session Configurator Network Switches.cc**: 2 switches
- **Components Ntp Tiles Switches.cc**: 1 switches
- **Components Optimization Guide Optimization Guide Switches.cc**: 27 switches
- **Components Page Content Annotations Page Content Annotations Switches.cc**: 5 switches
- **Components Regional Capabilities Regional Capabilities Switches.h**: 3 switches
- **Components Search Engines Search Engines Switches.cc**: 4 switches
- **Components Search Engines Search Engines Switches.h**: 1 switches
- **Components Search Provider Logos Switches.cc**: 3 switches
- **Components Ui Devtools Switches.cc**: 1 switches
- **Components Webui Flags Flags Ui Switches.cc**: 2 switches
- **Compositor**: 7 switches
- **Content Content Switches.cc**: 197 switches
- **Content Content Switches.cc, Policy**: 5 switches
- **Content Content Switches.cc, Ui Ui Switches.cc**: 3 switches
- **Crash**: 1 switches
- **DBus**: 10 switches
- **Demo**: 1 switches
- **Display**: 9 switches
- **Enterprise**: 2 switches
- **Events**: 2 switches
- **Extensions**: 27 switches
- **Feedback**: 1 switches
- **Fuchsia**: 12 switches
- **GCM**: 3 switches
- **Gaia**: 9 switches
- **Gamepad**: 1 switches
- **Gpu Command Buffer Client Gpu Switches.cc**: 2 switches
- **Gpu Command Buffer Service Gpu Switches.cc**: 19 switches
- **Gpu Command Buffer Service Gpu Switches.cc, Ui Gl Gl Switches.cc**: 1 switches
- **Gpu Config Gpu Switches.cc**: 47 switches
- **Gpu Config Gpu Switches.h**: 2 switches
- **Graphics**: 5 switches
- **Graphics, Headless**: 1 switches
- **HID**: 1 switches
- **Headless**: 22 switches
- **Headless, Shell**: 1 switches
- **Headless, Switches.cc**: 1 switches
- **I18n**: 4 switches
- **Infobars**: 1 switches
- **Input**: 3 switches
- **Keyboard**: 2 switches
- **Mahi**: 1 switches
- **Media Capture**: 2 switches
- **Media Media Switches.cc**: 34 switches
- **Metrics**: 9 switches
- **Modules**: 1 switches
- **Mojo**: 5 switches
- **Network Service**: 18 switches
- **Ozone**: 10 switches
- **Permissions**: 1 switches
- **Policy**: 19 switches
- **Predictors**: 1 switches
- **Safe Browsing**: 21 switches
- **Services Resource Coordinator Memory Instrumentation Switches.cc**: 2 switches
- **Services Service Manager Cpp Service Executable Switches.cc**: 2 switches
- **Services Service Manager Switches.cc**: 1 switches
- **Shell**: 8 switches
- **Signin**: 1 switches
- **Skia**: 2 switches
- **Switches.cc**: 22 switches
- **Sync**: 13 switches
- **Test**: 53 switches
- **Third Party Blink Switches.cc**: 35 switches
- **Third Party Blink Switches.h**: 5 switches
- **Tracing**: 19 switches
- **Translate**: 3 switches
- **Ui Gl Gl Switches.cc**: 22 switches
- **Ui Ui Switches.cc**: 13 switches
- **VR**: 3 switches
- **Variations**: 20 switches
- **Views**: 3 switches
- **Viz**: 10 switches
- **WebAuthn**: 3 switches
- **Window Manager**: 1 switches
- **iOS**: 15 switches

### Review Checklist
- [ ] All switches reviewed
- [ ] Important switches identified and tagged
- [ ] Deprecated switches noted
- [ ] Documentation gaps identified
- [ ] Follow-up actions documented