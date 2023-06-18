
 def f():
    fib_ratios = [0.382, 0.5, 0.618, 0.764, 1.272, 1.618, 2, 2.414]
    while True:
        high_low = input("Provide 'Hi, Lo' to get your levels: ")
        if high_low != 'exit':
            high = float(high_low.split(",")[0].strip())
            low = float(high_low.split(",")[1].strip())
            up, down = {}, {}
            for fr in fib_ratios:
                diff = high - ((high - low) * fr)
                fib_diff = high - diff
                if fr > 1:
                    up[fr] = [fib_diff + low, (((fib_diff + low) - high) / high) * 100]
                else:
                    down[fr] = [fib_diff + low, ((high - (fib_diff + low)) / high) * 100]
            print("UP:")
            for k, v in up.items():
                print("{:<6} - {:<10.5f} - {:.2f}%".format(k, v[0], v[1]))

            print('\nDOWN:')
            sorted_dict = dict(sorted(down.items(), key=lambda x: x[0], reverse=True))
            for k, v in sorted_dict.items():
                print("{:<6} - {:<10.5f} - {:.2f}%".format(k, v[0], v[1]))
            print()
        elif high_low == "exit":
            break
