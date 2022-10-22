# コマンドの設定方法 (macOS & Linux)
## macOSの場合  
- このディレクトリを <code> ~/ </code> 配下に設置する。  
```
$ mv shiro ~/shiro
```
- 権限を付与する。
```
$ chmod u+x ~/shiro/shiro
```
- PATHを通す。
```
$ echo export PATH='$PATH:$HOME/shiro/' >> ~/.zshrc
$ source ~/.zshrc
```

## Linux の場合 (Ubuntuを想定)
- このディレクトリを <code> ~/ </code> 配下に設置する。
```
$ mv shiro ~/shiro
```
- 権限を付与する。
```
$ chmod u+x ~/shiro/shiro
```
- PATHを通す。
```
$ echo export PATH='$PATH:$HOME/shiro/' >> ~/.bashrc
$ source ~/.bashrc
```

## 実行方法
```
$ shiro <ファイル名>(拡張子は入れない)
```
