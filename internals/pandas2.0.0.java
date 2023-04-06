index = pd.MultiIndex.from_product(
    [range(3), ["one", "two"]], names=["first", "second"]
)


index
Out[2]: 
MultiIndex([(0, 'one'),
            (0, 'two'),
            (1, 'one'),
            (1, 'two'),
            (2, 'one'),
            (2, 'two')],
           names=['first', 'second'])

index.levels
Out[3]: FrozenList([[0, 1, 2], ['one', 'two']])

index.codes
Out[4]: FrozenList([[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]])

index.names
Out[5]: FrozenList(['first', 'second'])
