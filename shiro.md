# 文法
shiro の基本型
```c
import stdio.h
func int main (void)
END
```
## 型・変数
shiro の型
- char (文字型)
- int (整数型)
- float (単精度浮動小数点型)
- double (倍精度浮動小数点型)

```c
import stdio.h
func int main (void)
	char a
	int b
	float c
	double d
	in a = "A"
	in b = 22
	in c = 33.33
	in d = 44.44
	retu 0
END
```
このように型宣言と代入を同時に行うこともできます。
```c
var int i = 50
```

## 演算
- 四則演算
```go
import stdio.h
func int main (void)
	printf "1+2=%d\n",1+2
	printf "4-3=%d\n",4-3
	printf "5*6=%d\n",5*6
	printf "6/2=%d\n",6/2
	printf "7/2の余り=%d\n",7%2
	retu 0
END
```
POINT: 空白を作ってはいけません。   
<br>
- scanf で入力を取ることができます。
```go
import stdio.h
func int main (void)
	int x
	printf "x="
	scanf "%d" &x
	printf "%d",x
	retu 0
END
```

## if文・条件分岐
shiro には switch文がありません。  
if 文だけを使用することで誰もが同じようなソースになり、読み書きが楽になります。
```go
import stdio.h
func int main (void)
	int a
	printf "数値を入力してください="
	scanf "%d" &a
	if a>10 
	{
		printf "入力した数値は,'10'より大きいです。\n"
	} 
	elif a>5
	{
		printf "入力した数値は,'5'より大きいです。\n"
	}
	else
	{
		printf "入力した数値は,'5'以下です。\n"
	}
	retu 0
END
```
```go
import stdio.h
func int main (void)
	int a
	printf "数値を入力してください="
	scanf "%d" &a
	if a>=10&&a<=20
	{
		printf "入力した数値は,'10以上','20以下'です。\n"
	}
	retu 0
END
```
## for文・繰り返し処理
shiro には while文がありません。  
for 文だけを使用することで誰もが同じようなソースになり、読み書きが楽になります。
```go
import stdio.h
func int main (void)
	int i
	var int sum = 0
	for i=0;i<=100;i++
	{
		printf "%d\n",i
		calc sum+=i
	}
	printf "\n合計=%d\n",sum
	retu 0
END
```
- continue;
```go
import stdio.h
func int main (void)
	int i
	for i=0;i<10;i++
	{
		if i==5
		{
			continue
		}
		if i==7
		{
			continue
		}
		printf "Hello!-%d\n",i
	}
	retu 0
END
```
- break;
```go
import stdio.h
func int main (void)
	int i
	for i=0;i<10;i++
	{
		printf "Hello!-%d\n",i
		if i==5 
		{
      		break
		}
	}
	retu 0
END
```

