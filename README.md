# BlackJack

![Python](https://img.shields.io/badge/Python-3.12-blue)
![CLI](https://img.shields.io/badge/interface-CLI-lightgrey)
![Status](https://img.shields.io/badge/status-in_progress-yellow)

## Overview

Python で実装したCLIベースのブラックジャックゲームです。
`Card`, `Deck`, `Hand`, `Player`, `Game` といったクラスに責務を分割し、オブジェクト指向を意識して実装しています。
ターミナルから実行し、ディーラーとのブラックジャックをプレイすることができます。

## Demo / Screenshot

実行画面、GIF、CLIの実行例、Web画面など。

## Features

- CLI上でブラックジャックをプレイできる
- 複数プレイヤーに対応
- 52枚のカードデッキを生成・シャッフル
- Hit / Stand の選択に対応
- Ace を 1 または 11 として扱うスコア計算
- プレイヤーとディーラーの勝敗判定

## Tech Stack

- Python 3.12.3

## Setup

```bash
git clone https://github.com/ShuichiFujii/BlackJack.git
cd BlackJack
```

## Usage

```bash
python3 main.py
```

1. プレイヤーの人数を入力します。
2. 各プレイヤーにカードが配られます。
3. プレイヤーはHit（カードを引く）かStand（カードを引かない）を選択します。
4. Stand するか、Bust（合計が21を超える）するまで、プレイヤーはHitを選択できます。
5. 全プレイヤーがStand するか、Bust した後、ディーラーのターンになります。
6. ディーラーがStandするか、Bustするまでカードを引きます。その後、ディーラーの手札が公開され、勝敗が決まります。

<!-- ## Tests

テストの実行方法。

## CI

GitHub Actionsなどで何を自動化しているか。 -->

## Project Structure

```text
BlackJack/
├── main.py
├── card.py # Card, Rank, Suit
├── deck.py # Deck
├── hand.py # Hand
├── player.py # Player
└── game.py # Game
```

## Design / Implementation Notes

このプロジェクトでは、ブラックジャックのゲームロジックをオブジェクト指向で実装しています。

主なクラスの責務は以下の通りです。

- `Card` クラスは、カードのランクとスートを表現します。
- `Deck` クラスは、52枚のカードを生成し、シャッフル
  する機能を提供します。
- `Hand` クラスは、プレイヤーの手札を管理し、スコアの計算や Bust 判定を行います。
- `Player` クラスは、プレイヤーの名前と手札を管理し、勝敗判定の機能を提供します。
- `Game` クラスは、ゲームの進行を管理し、プレイヤーのターンやディーラーのターンを制御します。

各クラスの責務を分けることで、ゲーム進行の処理とカード・手札などのデータ管理を分離します。

## Future Improvements

- pytest を導入し、スコア計算・Bust 判定・勝敗判定のテストを追加する
- 入力値のバリデーションを強化する
- ベット機能を追加する
- ゲーム結果の履歴を保存できるようにする
- API化し、Webアプリから利用できるようにする

## Author

- [Shuichi Fujii](https://github.com/ShuichiFujii)
- [Qiita](https://qiita.com/embermaverick05)
