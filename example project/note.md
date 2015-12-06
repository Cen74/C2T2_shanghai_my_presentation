# 示例项目开发记录

## 任务描述
已知有一个字典数据如下：

```python
adict = {
    'A1': 41
    'A3': 23
    'A9': 39
    'A10': 10
    'B1': -1
    'B2': -2
    'C5': '5'
    'C8': '8'
}
```

请通过python代码，输出一个列表，列表里的元素是字典里以'A'打头的键对应的值，且元素在列表中的顺序是根据对应键'A'后面跟的数值顺序进行排列。

即输出结果应当为：

```python
[41, 23, 39, 10]
```

## 任务分解

+ [X] 提取字典adict里所有以'A'开头的键，返回为一个列表keys_A_list
+ [ ] 按列表元素里的数字部分进行排序，返回顺序排列的列表ordered_keys_A_list
+ [ ] 根据ordered_key_list提取adict里对应的值，返回一个列表values_A_list

## step 1: pick_keys_from_dict
测试记录

| input | expected output | actual output | pass |
|---|---|---|---|---|
| {'A1':1,'B2':2,'C3':3} | ['A1'] | ['A1'] | √ |
| {'A1':1,'B2':2,'C3':3,'A4':4} | ['A1','A4'] | ['A1','A4'] | √ |

## step2: sorted_list_by_number_inside
测试记录:

| input | expected output | actual output | pass |
|---|---|---|---|---|
| ['A5', 'A3', 'A2'] | ['A5', 'A3', 'A2'] | ['A2', 'A3', 'A5'] | √ |
| ['A5', 'A20', 'A10'] | ['A10', 'A20', 'A5'] | ['A5', 'A20', 'A10']| x |

debug记录:

| Theory | input | E_output | A_output | confirmed |
| --- | --- | --- | --- |
| 元素被逆序排列 | ['A2', 'A5', 'A3'] | ['A3', 'A5', 'A2'] | ['A2', 'A3', 'A5'] |X |
| 元素里的数字被当做字符串类型进行排序 | ['A1', 'A11', 'A10'] | ['A1', 'A10', 'A11'] | ['A1', 'A10', 'A11'] | √ |

修改：
sorted_list = sorted(mylist, key=lambda x: int(x[1:]))

继续测试:

| input | expected output | actual output | pass |
|---|---|---|---|---|
| ['A5', 'A20', 'A10'] | ['A10', 'A20', 'A5'] | ['A10', 'A20', 'A5'] | √ |
| ['AB5', 'AB3', 'AB2'] | ['AB2', 'AB3', 'AB5'] | |

## step3: pick_values_from_dict
| input | expected output | actual output | pass |
|---|---|---|---|---|
| {'a':1,'b':2,'c':3}, ['a','b'] | [1,2] | [1,2] | √ |

测试 -> debug -> 修订 -> 测试