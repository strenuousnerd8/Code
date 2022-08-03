for _ in range(int(input())):
    N, X, Y, A, B = map(int, input().split())
    petrol = X * B
    diesel = Y * A
    print("PETROL" if diesel > petrol else "DIESEL" if diesel < petrol else "ANY")