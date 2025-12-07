from stock_linked import stock

if __name__ == "__main__":
    s = stock()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)
    s.traverse()
