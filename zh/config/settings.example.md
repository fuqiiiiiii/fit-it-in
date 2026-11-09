# 参数（示例）

> 模板。设置流程会原样复制成 `config/settings.md`。
> 这些默认值来自作者六周的每日实际使用。想改就用大白话说（「不加系数」「平日上限改成一半」），或者直接改文件。

```yaml
weekday_cap: 0.667      # 平日最多排当天空隙的 2/3，剩下的故意留白
weekend_cap: 0.333      # 休息日最多排 1/3
weekend_days: [sat, sun]   # 你的休息日，例如 [tue, wed]
buffer: 1.6             # 你的估计 × 1.6，因为事情通常比预想多花 60% 的时间
min_gap: 45             # 分钟；更短的空隙忽略
split_threshold: 180    # 分钟；更长的任务拆成 2–4 步
reminder_days: 3        # ddl 这么近、还没有块，brief 里会提一句
no_meal_hours: 4        # 连续忙这么久没机会吃饭，就标出来
chart_start: auto       # 图从几点开始画；auto = 起床那一小时
chart_end: auto         # 画到几点；auto = 睡觉那一小时
show_hints: true        # brief 最后加一行用法提示
```
