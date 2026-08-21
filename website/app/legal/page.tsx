export default function LegalDisclosure() {
  const rows = [
    ["販売業者（名称）", "NonMouse"],
    ["運営責任者", "請求があった場合、遅滞なく開示します。"],
    ["所在地", "消費者から請求があった場合、遅滞なく開示します。"],
    ["電話番号", "消費者から請求があった場合、遅滞なく開示します。"],
    ["メールアドレス", "kintre.ndy0@gmail.com"],
    ["販売URL", "https://nonmouse.com/"],
    ["提供内容", "NonMouse のソフトウェア利用権、早期アクセス、サポーター向けデジタル提供物、または特典なしの任意支援"],
  ];

  const sections = [
    ["販売価格", "各販売ページ、支援ページ、または決済ページに表示された価格（税込）に従います。"],
    ["商品代金以外の必要料金", "インターネット接続料、通信料、決済手数料等はお客様の負担となります。決済手数料が発生する場合は、各プラットフォームの表示に従います。"],
    ["支払方法・支払時期", "Buy Me a Coffee、Ko-fi、クレジットカード等、各プラットフォームが提供する決済方法に従います。購入または支援操作が完了した時点で決済されます。"],
    ["提供時期", "デジタル商品または早期アクセスは、販売ページに別段の記載がない限り、決済完了後に提供します。特典なしの任意支援については、対価に見合う商品・役務の提供はありません。"],
    ["返品・キャンセル・返金", "デジタルコンテンツの性質上、購入後の返品・キャンセル・返金は原則としてお受けしていません。ただし、二重決済、提供不能、販売ページの説明と著しく異なる場合は、個別に対応します。返金を希望する場合は、購入日、購入URL、理由を添えてメールでご連絡ください。各プラットフォームの規定の範囲で対応します。"],
    ["動作環境", "NonMouse の案内ページ、GitHub、配布ページ、または各販売ページに記載された環境に従います。"],
    ["所在地・電話番号・運営責任者の開示について", "所在地、電話番号および運営責任者は、消費者から請求があった場合、遅滞なく開示します。開示請求は上記メールアドレスまでご連絡ください。"],
    ["お問い合わせ", "メール: kintre.ndy0@gmail.com\n通常3営業日以内に返信します。"],
  ];

  return (
    <div className="min-h-screen bg-background py-24">
      <div className="container px-4 mx-auto max-w-3xl">
        <h1 className="text-4xl font-bold mb-6">特定商取引法に基づく表記</h1>
        <p className="text-muted-foreground mb-10">最終更新: 2026-08-21</p>

        <div className="space-y-10 text-base leading-8">
          <section>
            <h2 className="text-2xl font-semibold mb-6">販売業者</h2>
            <div className="space-y-6">
              {rows.map(([label, value]) => (
                <div key={label} className="border-b border-border pb-5">
                  <h3 className="font-semibold mb-2">{label}</h3>
                  <p className="whitespace-pre-line text-muted-foreground">{value}</p>
                </div>
              ))}
            </div>
          </section>

          {sections.map(([title, body]) => (
            <section key={title}>
              <h2 className="text-2xl font-semibold mb-4">{title}</h2>
              <p className="whitespace-pre-line text-muted-foreground">{body}</p>
            </section>
          ))}
        </div>
      </div>
    </div>
  );
}
