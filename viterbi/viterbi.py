from collections import Counter


outer_status = {'正常':0,'头晕':1,'发冷':2}
inner_status = {'健康':0,'发烧':1}
inner_status_len = len(inner_status)


def main():
    inner_table = [[0.7,0.3],[0.4,0.6]]
    outer_table = [[0.5,0.1,0.4],[0.1,0.6,0.3]]
    start_to_others = [0.6,0.4]
    outer_sequences = [outer_status['正常'],outer_status['发冷'],outer_status['头晕']]
    sequences_len = len(outer_sequences)

    # 计算结果存放表
    table = [[None]*inner_status_len for _ in range(sequences_len)]
    temp = [0.0] * sequences_len
    for i in range(inner_status_len):
        # 第一层手动算，None表示这是第一层，前面没有再多的
        table[0][i] = [start_to_others[i] * outer_table[i][outer_sequences[0]],None]
    for layer_i in range(1,sequences_len):
        pre_layer = layer_i - 1
        for current_j in range(inner_status_len):
            for pre_k in range(inner_status_len):
                temp[pre_k] = table[pre_layer][pre_k][0] * inner_table[pre_k][current_j] * outer_table[current_j][outer_sequences[layer_i]]

            min_value = max(temp)
            min_index = temp.index(min_value)
            table[layer_i][current_j] = [min_value,min_index]

    print(table)

    # 下面这大段是反向查找
    lastest_values = []
    for value in table[-1]:
        lastest_values.append(value[0])
    index = lastest_values.index(max(lastest_values))

    inner_sequence = []
    inner_sequence.append(index)
    layer = sequences_len - 1
    while True:
        index = table[layer][index][1]
        if index is None:
            break
        else:
            inner_sequence.append(index)
        layer -= 1

    inner_sequence.reverse()
    print(inner_sequence)


if __name__ == '__main__':
    main()
