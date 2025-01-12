# UHAILab
for the AI Lab course at the University of Helsinki in 2025

# Introduction
This is the page for storing some tips.

# Connecting with local computers
For more information, see Cloning a repository[1] and Set up Git[2].
[1] https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
[2] https://docs.github.com/en/get-started/getting-started-with-git/set-up-git

# Fork
Git has its own strong power/function to copy easily other's project. This is helped by forking. For more information, see Fork a repository[3].
[3] https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo

# Computing Coverage[4]
カバレッジとは、対象範囲に対して全体の内どれくらい網羅しているかを示す指標です。「網羅率」と表現されることもあり、さまざまな業界で利用される言葉です。

ソフトウェア開発の領域では主に、テストの実施状況を評価する方法を示す言葉として使われます。ホワイトボックステスト時に用いられることが多く、論理構造全体に対してどれだけの実行ができたかの網羅性の尺度として使用されます。網羅性を把握することがソフトウェアの品質において重要な指標になります。

カバレッジ基準の種類として、さまざまなものがありますが、ソフトウェアテストとしてよく利用されるのは、以下の３つのカバレッジになります。

・ステートメントカバレッジ（C0）
・デシジョンカバレッジ（C1）
・複合条件カバレッジ（C2）

ステートメントカバレッジ（C0）とは、「命令文」に着目したカバレッジ基準のことです。「命令網羅率」ともいい、すべての命令文を最低一度は通るようにテストします。

命令文を一度通るだけであるためカバレッジレベルは本記事で紹介するものの中ではもっとも低く、テスト量も比較的少ないという特徴があります。テスト量が少なくなるためそのため、導入しやすい基準かもしれません。

ステートメントカバレッジは、命令のみに着目するため、例えば条件を満たす方にだけ命令のある条件文では、条件を満たす場合のみをテストすれば、カバレッジを網羅したことになります。そのため、ステートメントカバレッジで100％網羅したとしても、条件を満たさない（ELSE）ルートに不具合がある場合はテスト漏れになる可能性があります。ステートメントカバレッジでは、実質的な網羅性・テスト強度は低いといえるでしょう。

デシジョンカバレッジ（C1）とは、「分岐した経路」に着目したカバレッジ基準です。すべての分岐条件や真・偽などの経路を最低一度は通るようにテストします。

分岐した経路をすべて通るため、ステートメントカバレッジよりもカバレッジレベルが高いことが分かります。

デシジョンカバレッジでは、条件文としての成立と不成立の両方に着目してカバレッジを判断します。ただし、条件式中に論理和（OR）や論理積（AND）などが含まれる複合条件どうかについては考慮がありません。そのため、複合条件の判定式の不具合を検出できない可能性がある点に注意しなければなりません。

複合条件カバレッジ（C2）とは、「条件」に着目したカバレッジ基準です。コード内に含まれているすべての条件パターンをテストし、正しく動作するかを確認します。複合条件の場合は、それを構成する個々の条件の、成立・不成立の組み合わせをすべてテストします。

すべての条件パターンを満たすこの基準は上位のカバレッジレベルですが、上位のカバレッジレベル基準は下位のカバレッジ基準を包含する関係にあります。複合条件カバレッジを満たしている場合は、デシジョンカバレッジ、ステートメントカバレッジも確保されます。

下位のカバレッジ基準では判定できなかった部分が明確になるため、テスト基準としては強度が高いといえるでしょう。反面、条件式が増えるほどテストケースの数も増える点に注意が必要です。

# Unit Test[5]
https://medium.com/swlh/a-simple-guide-to-automating-unit-tests-in-python-3738cf049238

ユニットテストとは、ソフトウェアを日々開発、修正していく中でその品質を確保する「テストツール」です。テスト実行は自動化が可能なので、長期的に見ればテスト工数を削減できます。しかし、つまりそれはテストコードの開発が必要であることを意味します。

割と社会でよくあるのが、開発工数や期間が足りないのでユニットテストは作成せず人手によるマニュアルテストでやりのけていくというケースらしいです。
