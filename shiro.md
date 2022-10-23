# 文法
### はじめに。
shiro では、空白がとても重要です。  
文字列などで空白を使用してはいけません。  
関係式等でも <code>, </code>などの空白を許容しません。  
うまく動作しない場合は、一度確認してみましょう。  
<br>
shiro の基本型
```c
import stdio.h
func int main void
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
func int main void
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
func int main void
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
func int main void
	int x
	printf "x="
	scanf "%d" &x
	printf "%d",x
	retu 0
END
```

## if else 文・条件分岐
if else 文 と switch 文 があります。
- if else 
```go
import stdio.h
func int main void
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
- switch 
```go
import stdio.h
func int main void
	int a
	printf "数値を入力してください。>>>"
	scanf "%d" &a
	switch a
	{
		case 0
			printf "0だよ。\n"
			break
		case 1
			printf "1だよ。\n"
			break
		case 2
			printf "2だよ。\n"
			break
		case 3
			printf "3だよ。\n"
			break
		case 4
			printf "4だよ。\n"
			break
		case 5
			printf "5だよ。\n"
			break
		default
			printf "それ以外だよ。"
			break
	}
	retu 0
END
```
## for 文・繰り返し処理
for 文 と while 文 があります。
- for
```go
import stdio.h
func int main void
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
- for (continue;)
```go
import stdio.h
func int main void
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
- for (break;)
```go
import stdio.h
func int main void
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
- while (shiro では loop と言います。)  
POINT: 式を書く時はいつでも <code>calc</code> を使用します。
```go
import stdio.h
func int main void
	var int i = 1
	var int sum = 0
	loop sum<100
	{
		calc sum=sum+i
		printf "(i,sum)=(%d,%d)",i,sum
		calc i=i+1
	} 
	retu 0
END
```
## おまけ 
### rand 関数 を使ってみよう。
```go
import stdio.h
import stdlib.h
func int main void
	int i
	printf "◆3つの乱数を生成\n"
	for i=0;i<3;i++
	{
		printf "%dつ目の乱数=%d\n",i+1,rand()
	}
	// 乱数の最大値を表示
	in i = RAND_MAX
	printf "\n◆乱数の最大値を表示\n"
	printf "RAND_MAX=%d\n",i
	retu 0
END
```