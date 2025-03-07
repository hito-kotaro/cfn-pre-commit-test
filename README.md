# Python Lambda CloudFormation テンプレート

このプロジェクトは、AWS SAM（Serverless Application Model）を使用して Python Lambda 関数をデプロイするためのテンプレートを提供します。

## プロジェクト構成

```
.
├── template.yaml                # SAMテンプレート
├── lambda_function/             # Lambda関数のコードディレクトリ
│   └── index.py                 # Lambda関数のメインコード
├── .githooks/                   # Gitフックディレクトリ
│   └── pre-commit               # コミット前に実行されるスクリプト
└── README.md                    # このファイル
```

## セットアップ手順

### リポジトリのクローン後の設定

リポジトリをクローンした後、以下のコマンドを実行して Git hooks のパスを設定してください：

```bash
git config core.hooksPath .githooks
```

この設定により、コミット時に自動的に CloudFormation テンプレートのバリデーションが実行されます。

## Git pre-commit フックについて

このプロジェクトでは、Git の pre-commit フックを使用して、コミット前に以下のチェックを自動的に実行します：

- AWS CloudFormation validate-template コマンドによるテンプレートの検証
- cfn-lint によるテンプレートの lint チェック（W3002 警告は無視）
- Lambda 関数の CodeUri パスが存在するかのチェック

手動でフックをテストするには：

```bash
./.githooks/pre-commit
```

## 前提条件

- AWS CLI がインストールされ、設定されていること
- cfn-lint がインストールされていること（テンプレートの検証用）
