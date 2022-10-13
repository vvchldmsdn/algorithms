from pprint import pprint


def solution(commands):
    food_graph = dict()
    board = dict()
    merge = dict()

    for command in commands:
        detail = command.split(' ')
        if detail[0] == 'UPDATE':
            if len(detail) == 4:
                x = int(detail[1])
                y = int(detail[2])
                idx = (x-1)*50 + y
                thing = detail[3]
                board[idx] = thing

                if idx in merge:
                    for target in merge[idx]:  # 연결되어있는거 다 바꿈
                        board[target] = thing
                        if thing not in food_graph:
                            food_graph[thing] = [target]
                        else:
                            food_graph.append(target)

                if thing not in food_graph:
                    food_graph[thing] = [idx]
                else:
                    food_graph[thing].append(idx)
            else:
                for target in food_graph[detail[1]]:
                    number = (target[0] - 1) * 50 + target[1]
                    board[number] = detail[2]

        elif detail[0] == 'MERGE':
            first = (int(detail[1]) - 1) * 50 + int(detail[2])
            second = (int(detail[3]) - 1) * 50 + int(detail[4])

            if first in merge:
                merge[first].append(second)
            else:
                merge[first] = [second]
            if second in merge:
                merge[first].extend(merge[second])
            merge[first] = list(set(merge[first]))

            if second in merge:
                merge[second].append(first)
            else:
                merge[second] = [first]
            if first in merge:
                merge[second].extend(merge[first])
            merge[second] = list(set(merge[second]))

            for target in merge[first]:
                board[target] = board[first]

        elif detail[0] == 'UNMERGE':
            x = int(detail[1])
            y = int(detail[2])
            idx = (x - 1) * 50 + y
            for target in merge[idx]:
                thing = board[target]
                food_graph[thing].pop(food_graph[thing].index(idx))
                del board[target]
        print(board)
        print('merge', merge)
    pprint(merge)

    answer = []
    return answer


print(solution(['UPDATE 1 1 a', 'UPDATE 1 2 b', "UPDATE 2 1 c", 'UPDATE 2 2 d',
      'MERGE 1 1 1 2', 'MERGE 2 2 2 1', 'MERGE 2 1 1 1', 'PRINT 1 1', 'UNMERGE 2 2', 'PRINT 1 1']))
