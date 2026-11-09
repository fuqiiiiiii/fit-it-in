# 个人配置（示例）

> 模板。设置流程会把它复制成 `config/profile.md`，填上你的信息。
> 下面全部是虚构的示例。`profile.md` 可以直接改，也可以用大白话告诉 Claude。

## 基本信息

```yaml
language: zh                     # zh | en
timezone: Asia/Shanghai
email: xiaolin@example.com       # brief 的邮件版发到这里
brief_time: "07:00"
delivery: [email, session]       # 或 [session]
deadline_prefix: "DDL · "        # 计划日历上 ddl 事件的标题前缀
```

## 日历

```yaml
fixed_calendars:                 # 只读
  - 课程表
  - 社团活动
planner_calendar: xiaolin@example.com   # Claude 唯一会写入的日历
anchors:                         # 计划日历上的重复习惯；占时间，但永远不记账
  - 健身
  - 跑步
```

## 作息

不想让 Claude 按某项来排，就留空。留空不会被当成 Claude 编出来的空闲时间，只是不扣而已。

```yaml
wake: "07:00"
sleep: "23:00"
meals:
  breakfast: { mon-fri: "07:30-08:00", sat-sun: "09:00-09:30" }
  lunch:     { all: "12:00-12:45" }
  dinner:    { all: "18:00-18:45" }
commute:
  minutes: 20                    # 单程
  leave:   { mon: "08:20", wed: "08:20", fri: "09:30" }
  # 没列出的日子 = 不通勤
```

## 固定重复事项（兜底）

每周都有、但日历里可能漏掉的事。哪天日历里没有，Claude 会自己补上。

| 星期 | 事项 | 时间 | 地点 |
|---|---|---|---|
| 周五 | 实验课 | 14:00–15:30 | 理科楼 210 |

## 补充规则（大白话）

一行一条。上面的字段写不下的，都写在这里。

- 健身那天（周一、周四），午饭挪到健身之后。
- 周日 21:30 以后不排工作。

## 不管的事

这个 planner 永远不排、也不提的事。

- 生活杂事（我用别的提醒 app）
- 发社交媒体
