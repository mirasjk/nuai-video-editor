"""Generate the dependency-free Turkish and English NU AI product pages."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent
REPO = "https://github.com/uceribasi/nuai-video-editor"
DOWNLOAD = REPO + "/releases/download/v0.1.0/nuai_0.1.0_aarch64.dmg"

CONTENT = {
    "tr": {
        "title": "NU AI Video Editor — Kayıtlarını temizle. Hikâyen kalsın.",
        "description": "Mac için ücretsiz, açık kaynak video editörü. Duraklamaları, tekrar çekimleri ve dolgu kelimelerini temizle; altyazı, çeviri ve beta dublaj ekle.",
        "skip": "İçeriğe geç", "nav": ["Nasıl çalışır", "Özellikler", "Sorular"],
        "download": "Mac için indir", "downloadFree": "Mac için ücretsiz indir", "menu": "Menüyü aç",
        "eyebrow": "DAHA AKICI KAYITLAR. DAHA AZ UĞRAŞ.",
        "headline": "Anlatacakların kalsın.<br><em>Gerisini NU AI temizlesin.</em>",
        "intro": "Duraklamaları, tekrarları ve dolgu kelimelerini temizle. Altyazı ekle, çevir ve kendi sesinle dublaj yap. Hepsi Mac’inde.",
        "seeDemo": "Nasıl çalıştığını gör",
        "meta": "Apple Silicon · macOS 11+ · v0.1.0",
        "badges": ["Ücretsiz ve açık kaynak", "Mac’inde yerel analiz", "Kontrol her zaman sende"],
        "sample": "Örnek iş akışı", "original": "Kayıt", "edited": "Temizlenmiş",
        "sceneLabel": "KONUŞMA KAYDI", "transcriptLabel": "TRANSKRİPT", "suggestion": "Kesim önerileri",
        "sentence": '<span class="word-cut">Eee,</span> bugün size <span class="word-retake">yeni uygulamayı… baştan alayım.</span> <span class="word-pause">2.4 sn</span> Videolarınızı daha akıcı hâle getirmenin kolay bir yolunu göstereceğim.',
        "caption": '<del>Eee,</del> videolarınızı daha akıcı hâle getirin.',
        "legend": ["Tekrar", "Duraklama", "Dolgu kelimesi"], "timeline": "ZAMAN ÇİZELGESİ",
        "beforeState": "Kayıt görünümü", "afterState": "Kesimler atlandı",
        "beforeResult": "Örnek kayıt · 00:30", "afterResult": "Örnek sonuç · 00:17",
        "demoNote": "Etkileşimli iş akışı gösterimi; bir video analizi değildir.",
        "demoRight": "Kayıt / Temizlenmiş düğmeleriyle karşılaştır.",
        "flowEyebrow": "VİDEODAN YAYINA",
        "flowTitle": "Çekimini bitir.<br>Kurguyu hafiflet.",
        "flowLead": "Konuşmaya odaklan. NU AI, kaydındaki gereksiz kısımları bulur; son kararı sen verirsin.",
        "steps": [
            ["Videonu aç", "Kaydını içeri al. Konuşma ve duraklamalar bilgisayarında analiz edilsin."],
            ["Kesimleri gözden geçir", "Transkript ve zaman çizelgesinde önerilen her kesimi kontrol et, tut veya çıkar."],
            ["Hazır olduğunda dışa aktar", "Akıcı videonu MP4 olarak al. İstersen altyazı ve farklı dilde ses izleri ekle."]
        ],
        "featuresEyebrow": "BİR KAYITTAN DAHA FAZLASI",
        "featuresTitle": "Gereksiz kısımlar gider.<br>Anlatımın güçlenir.",
        "featuresLead": "Temizleme, altyazı ve dışa aktarma aynı yerde. Aşağıdaki görüntüler doğrudan NU AI uygulamasından.",
        "gallery": [
            {"label": "Akıllı temizleme", "image": "review.png", "title": "Her kesimin bir nedeni var.", "description": "Duraklamalar, yanlış başlangıçlar, dolgu sesleri, tekrar eden kelimeler ve konuşma olmayan donmuş görüntüler. Her öneriyi kaynağıyla gör ve tek tek karar ver.", "alt": "NU AI inceleme ekranı: transkript, kesim önerileri ve video zaman çizelgesi. Görüntüde test videosu kullanılıyor."},
            {"label": "Altyazı ve dublaj", "image": "subtitles.png", "title": "Aynı hikâye. Başka bir dil.", "description": "Kesimlerine uyan altyazılar oluştur, seçtiğin AI ile çevir. İsteğe bağlı yerel ses motoruyla konuşmacının kendi sesinde dublaj ekle. Ses klonlama ve dublaj beta aşamasında.", "alt": "NU AI altyazı ekranı: çevrilmiş İngilizce altyazılar ve beta dublaj seçenekleri."},
            {"label": "Esnek dışa aktarma", "image": "export.png", "title": "Sonraki adımına hazır.", "description": "Altyazıları görüntüye yaz, seçilebilir dil izleri olarak ekle veya SRT/VTT dosyası al. Dublajı asıl sesin yerine ya da ek bir ses izi olarak dışa aktar.", "alt": "NU AI dışa aktarma penceresi: video, altyazı ve dublaj ses izi ayarları."}
        ],
        "expand": "Ekranı büyüt", "close": "Kapat",
        "privacyEyebrow": "KAYDIN SENİNLE KALSIN",
        "privacyTitle": "Videon buluta gitmez.<br>İş Mac’inde biter.",
        "privacyBody": "Yazıya dökme, konuşma algılama ve ses klonlama bilgisayarında çalışır. İsteğe bağlı AI incelemesi ve çeviri için yalnızca transkript metni seçtiğin sağlayıcıya gönderilir.",
        "privacyRows": [["Video ve ses", "Mac’inde"], ["Konuşma modeli", "Yerel"], ["İsteğe bağlı AI", "Yalnızca metin"]],
        "privacyFoot": "API anahtarınla bir sağlayıcı veya Ollama / LM Studio gibi yerel bir model kullanabilirsin.",
        "downloadEyebrow": "BİR SONRAKİ KAYDIN İÇİN",
        "downloadTitle": "Mac’ine yeni bir<br>kurgu yardımcısı.",
        "downloadIntro": "Ücretsiz indir, kendi kaydınla dene. Temel temizleme için AI sağlayıcısı veya API anahtarı gerekmez.",
        "appMeta": "Apple Silicon (M1 ve sonrası)<br>macOS 11 veya üzeri · DMG, 15.7 MiB",
        "release": "v0.1.0 sürüm notları",
        "install": [
            ["İndir ve Uygulamalar’a taşı", "DMG dosyasını aç ve nuai uygulamasını Uygulamalar klasörüne sürükle."],
            ["ffmpeg’i kur", "Homebrew kullanıyorsan aşağıdaki komutla kurabilirsin."],
            ["Konuşma modelini indir", "Uygulamada Ayarlar → Yazıya dökme bölümünden bir model seç. Önerilen model yaklaşık 547 MB."]
        ],
        "copy": "Komutu kopyala", "copied": "Komut kopyalandı.", "selectCommand": "Komutu seçip kopyalayabilirsin.",
        "installNote": 'Uygulama henüz Apple’ın notarization sürecinden geçmedi. İlk açılış için <a href="' + REPO + '#install" target="_blank" rel="noopener noreferrer">kurulum rehberine</a> göz at. Intel Mac’ler için kaynak koddan derleme seçeneği mevcut.',
        "faqEyebrow": "AKLINDA KALMASIN",
        "faqTitle": "Küçük sorular.<br>Net cevaplar.",
        "faq": [
            ["NU AI gerçekten ücretsiz mi?", "Evet. NU AI, MIT lisansıyla yayımlanan ücretsiz ve açık kaynak bir uygulama. Kendi API sağlayıcını kullanırsan sağlayıcının kullanım ücretleri ayrıca geçerli olabilir."],
            ["Windows veya Linux’ta kullanabilir miyim?", "Hazır indirme paketi şu anda Apple Silicon Mac’ler için. Windows ve Linux paketleri planlanıyor. Intel Mac’te uygulamayı kaynak koddan derleyebilirsin."],
            ["AI kullanmak zorunda mıyım?", "Hayır. Yerel yazıya dökme, duraklama algılama ve temel temizleme AI sağlayıcısı olmadan çalışır. AI incelemesi, hedef süreye kısaltma ve çeviri için seçtiğin sağlayıcı kullanılır."],
            ["Videolarım bir sunucuya yükleniyor mu?", "Ses ve video dosyaların yerel olarak işlenir. İsteğe bağlı bulut AI özelliklerini açtığında yalnızca transkript metni seçtiğin sağlayıcıya gider. Yerel bir model de kullanabilirsin."],
            ["Dublaj özelliği nasıl çalışıyor?", "Beta dublaj, videodaki konuşmacının sesinden bir referans alıp çevrilmiş altyazıları bu sesle okur; arka planı koruyarak bir ses izi oluşturur. İsteğe bağlı yerel ses motoru yaklaşık 4.5 GB indirme gerektirir. Yalnızca sana ait veya kullanma iznin olan sesleri klonlamalısın."],
            ["Bir kesimi geri çevirebilir miyim?", "Evet. İnceleme modunda önerilen kesimleri tek tek tutabilir veya kaldırabilirsin. Kendi kelime seçimlerinle de kesim yapabilir, sonucu dışa aktarmadan önce önizleyebilirsin."]
        ],
        "finalTitle": "Kayıt bitti.<br>Şimdi akıcı hâle gelsin.",
        "footerLicense": "Açık kaynak · MIT", "footerLinks": ["Kaynak kodu", "Geri bildirim", "Sürüm notları"],
    },
    "en": {
        "title": "NU AI Video Editor — Keep your story. Lose the extra takes.",
        "description": "A free, open-source video editor for Mac. Remove pauses, retakes and filler words. Add translated subtitles and optional local voice dubbing.",
        "skip": "Skip to content", "nav": ["How it works", "Features", "Questions"],
        "download": "Download for Mac", "downloadFree": "Download free for Mac", "menu": "Open menu",
        "eyebrow": "SMOOTHER RECORDINGS. LESS BUSYWORK.",
        "headline": "Keep your story.<br><em>Lose the extra takes.</em>",
        "intro": "Clean up pauses, retakes and filler words. Add subtitles, translate them and dub in your own voice. Right on your Mac.",
        "seeDemo": "See how it works",
        "meta": "Apple Silicon · macOS 11+ · v0.1.0",
        "badges": ["Free and open source", "Local analysis on your Mac", "Every cut is your call"],
        "sample": "Workflow example", "original": "Recording", "edited": "Cleaned up",
        "sceneLabel": "TALKING-HEAD RECORDING", "transcriptLabel": "TRANSCRIPT", "suggestion": "Suggested cuts",
        "sentence": '<span class="word-cut">Um,</span> today I’ll show you <span class="word-retake">the new app… let me start over.</span> <span class="word-pause">2.4 sec</span> An easier way to make your recordings feel more natural.',
        "caption": '<del>Um,</del> make your recordings feel more natural.',
        "legend": ["Retake", "Pause", "Filler word"], "timeline": "TIMELINE",
        "beforeState": "Original recording", "afterState": "Cuts skipped",
        "beforeResult": "Sample recording · 00:30", "afterResult": "Sample result · 00:17",
        "demoNote": "Interactive workflow illustration, not a live video analysis.",
        "demoRight": "Compare with the Recording / Cleaned up buttons.",
        "flowEyebrow": "FROM RECORDING TO READY",
        "flowTitle": "Finish recording.<br>Lighten the edit.",
        "flowLead": "Focus on what you have to say. NU AI finds the extra parts in your recording. You make the final call.",
        "steps": [
            ["Open your video", "Bring in your recording. Speech and pauses are analyzed locally on your computer."],
            ["Review the suggestions", "See every proposed cut on the transcript and timeline. Keep it, remove it, or make your own."],
            ["Export when you’re ready", "Get a smoother MP4. Add subtitles and extra language tracks when your story needs them."]
        ],
        "featuresEyebrow": "MORE FROM EVERY RECORDING",
        "featuresTitle": "Less of the extra.<br>More of your story.",
        "featuresLead": "Cleanup, subtitles and export in one place. These are real screenshots from the NU AI app.",
        "gallery": [
            {"label": "Smart cleanup", "image": "review.png", "title": "There’s a reason for every cut.", "description": "Pauses, false starts, filler sounds, accidental repeats and frozen footage where nobody is speaking. See why each cut was suggested and decide what stays.", "alt": "NU AI review screen with a transcript, proposed cuts and video timeline. The screenshot uses a test video."},
            {"label": "Subtitles & dubbing", "image": "subtitles.png", "title": "Same story. Another language.", "description": "Create subtitles that follow your cuts and translate them with your chosen AI. The optional local voice engine can dub in the speaker’s voice. Voice cloning and dubbing are in beta.", "alt": "NU AI subtitles screen showing translated English captions and beta dubbing controls."},
            {"label": "Flexible export", "image": "export.png", "title": "Ready for your next step.", "description": "Burn captions into the picture, add selectable subtitle tracks or export SRT/VTT files. Export a dub in place of the original audio or as an additional audio track.", "alt": "NU AI export dialog showing video, subtitle and dubbed audio options."}
        ],
        "expand": "View full screen", "close": "Close",
        "privacyEyebrow": "YOUR RECORDING STAYS WITH YOU",
        "privacyTitle": "Your video stays local.<br>Your Mac does the work.",
        "privacyBody": "Transcription, speech detection and voice cloning run on your computer. Optional AI review and translation send only transcript text to the provider you choose.",
        "privacyRows": [["Video and audio", "On your Mac"], ["Speech model", "Local"], ["Optional AI", "Text only"]],
        "privacyFoot": "Bring your own API provider or use a local model with Ollama or LM Studio.",
        "downloadEyebrow": "FOR YOUR NEXT RECORDING",
        "downloadTitle": "A new editing<br>companion for your Mac.",
        "downloadIntro": "Download for free and try your own recording. Basic cleanup needs no AI provider or API key.",
        "appMeta": "Apple Silicon (M1 or later)<br>macOS 11 or newer · DMG, 15.7 MiB",
        "release": "v0.1.0 release notes",
        "install": [
            ["Download and move to Applications", "Open the DMG and drag the nuai app into your Applications folder."],
            ["Install ffmpeg", "If you use Homebrew, run the command below."],
            ["Download a speech model", "Choose a model in Settings → Transcription inside the app. The recommended model is about 547 MB."]
        ],
        "copy": "Copy command", "copied": "Command copied.", "selectCommand": "Select the command to copy it.",
        "installNote": 'The app is not Apple-notarized yet. See the <a href="' + REPO + '#install" target="_blank" rel="noopener noreferrer">installation guide</a> for the first launch. Intel Mac users can build from source.',
        "faqEyebrow": "GOOD TO KNOW",
        "faqTitle": "Small questions.<br>Clear answers.",
        "faq": [
            ["Is NU AI really free?", "Yes. NU AI is free and open source under the MIT license. If you use your own API provider, that provider’s usage charges may apply separately."],
            ["Can I use it on Windows or Linux?", "The ready-to-install download is currently for Apple Silicon Macs. Windows and Linux packages are planned. Intel Mac users can build the app from source."],
            ["Do I have to use AI?", "No. Local transcription, pause detection and basic cleanup work without an AI provider. AI review, target-length shortening and translation use your chosen provider."],
            ["Are my videos uploaded to a server?", "Video and audio files are processed locally. If you enable optional cloud AI features, only transcript text is sent to your chosen provider. You can also use a local model."],
            ["How does dubbing work?", "Beta dubbing takes a voice reference from the speaker in your video and uses it to speak translated captions while preserving the background. The optional local voice engine requires about a 4.5 GB download. Only clone voices you own or have permission to use."],
            ["Can I reject a suggested cut?", "Yes. In Review mode you can keep or remove each suggested cut, select words to make your own cuts and preview the result before exporting."]
        ],
        "finalTitle": "The recording is done.<br>Let’s make it flow.",
        "footerLicense": "Open source · MIT", "footerLinks": ["Source code", "Feedback", "Releases"],
    }
}

PATHS = {
    "arrow": '<path d="M4 8h8M9 4l4 4-4 4"/>',
    "download": '<path d="M8 2v8m-3-3 3 3 3-3M3 11v3h10v-3"/>',
    "check": '<path d="m3 8 3 3 7-7"/>',
    "lock": '<rect x="3" y="7" width="10" height="7" rx="2"/><path d="M5 7V5a3 3 0 0 1 6 0v2"/>',
    "file": '<path d="M9 2H4v12h8V5L9 2Z"/><path d="M9 2v3h3M6 8h4M6 11h4"/>',
    "cut": '<circle cx="4" cy="4" r="2"/><circle cx="4" cy="12" r="2"/><path d="m6 5 7 8M6 11l7-8"/>',
    "video": '<rect x="2" y="3" width="9" height="10" rx="2"/><path d="m11 6 3-2v8l-3-2"/>',
    "expand": '<path d="M2 6V2h4m4 0h4v4M2 10v4h4m4 0h4v-4"/>',
    "copy": '<rect x="5" y="5" width="8" height="9" rx="1"/><path d="M10 3V2H2v9h1"/>',
    "sound": '<path d="M2 7v2h3l4 4V3L5 7H2ZM12 5a4 4 0 0 1 0 6"/>',
    "spark": '<path d="m8 2 1.5 4.5L14 8l-4.5 1.5L8 14 6.5 9.5 2 8l4.5-1.5L8 2Z"/>',
    "menu": '<path d="M2 4h12M2 8h12M2 12h12"/>',
}

def icon(name):
    return '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + PATHS[name] + '</svg>'

SCENE = """
<svg class="scene-art" viewBox="0 0 620 300" aria-hidden="true" preserveAspectRatio="xMidYMid slice">
<defs><linearGradient id="wall" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#e8e1d7"/><stop offset="1" stop-color="#c9ccd4"/></linearGradient><linearGradient id="shirt" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#9b8fc7"/><stop offset="1" stop-color="#6a5c94"/></linearGradient></defs>
<path fill="url(#wall)" d="M0 0h620v300H0z"/><rect x="395" y="0" width="3" height="250" fill="#ccd0d0"/><rect x="430" y="38" width="130" height="159" rx="2" fill="#d7dbe0"/><path d="M495 38v159m-65-83h130" stroke="#eef0ed" stroke-width="7"/><path d="M435 45h50v60h-50z" fill="#e6e8e4"/><rect x="74" y="56" width="88" height="114" rx="3" fill="#d4d2c9"/><rect x="81" y="63" width="74" height="100" rx="1" fill="#eeece4"/><path d="M99 144V86h37v58z" fill="#c8c5ba"/><path d="m99 144 13-40 24 40" fill="#a9afa0"/><ellipse cx="318" cy="289" rx="115" ry="16" fill="#656b6820"/>
<path d="M218 300v-45c0-52 30-79 83-79s91 26 91 79v45z" fill="url(#shirt)"/><path d="M282 166v24c0 15 39 15 39 0v-27z" fill="#c9a18d"/><path d="M259 97c0-40 85-42 85 0v41c0 31-20 48-43 48-23 0-42-17-42-48z" fill="#d5b39f"/><path d="M258 113c-10-18-7-53 15-62 27-18 60-7 72 18 5 12 4 29-3 40l-5-31c-22 13-42 3-57 0l-15 17z" fill="#484440"/><path d="M281 119h5m32 0h5" stroke="#66574e" stroke-width="3" stroke-linecap="round"/><path d="M296 135h7m-17 16c8 5 17 5 25 0" fill="none" stroke="#a37b69" stroke-width="2" stroke-linecap="round"/>
<path d="M219 295c8-37 11-62 32-66m140 66c-4-36-11-61-30-67" fill="none" stroke="#5f537e" stroke-width="3"/><path d="m265 299 35-39 39 39" fill="#d1b09e"/><path d="M0 280h620v20H0z" fill="#a4a196"/><path d="M170 281h31v-50h-31z" fill="#aaa395"/><path d="M185 234c-39-24-25-61-21-61 23 13 28 28 21 61M185 230c34-13 42-39 34-48-25 5-39 24-34 48" fill="#838d77"/><path d="M443 280v-75l-41-25" fill="none" stroke="#515655" stroke-width="5"/><rect x="383" y="152" width="25" height="52" rx="12" fill="#555a59" transform="rotate(-20 396 178)"/><path d="m384 173 24 8m-27-2 24 8m-20-20 24 8" stroke="#7a7e7b" stroke-width="2"/>
</svg>"""

def generate(lang):
    c = CONTENT[lang]
    p = "../" if lang == "en" else ""
    tr_url, en_url = ("../", "./") if lang == "en" else ("./", "en/")
    def asset(file): return p + "assets/" + file
    def link(label, cls="button", extra=""):
        return '<a class="' + cls + '" href="' + DOWNLOAD + '" ' + extra + '>' + icon("download") + escape(label) + "</a>"
    mode_buttons = '<button type="button" data-demo="before" aria-pressed="true">' + c["original"] + '</button><button type="button" data-demo="after" aria-pressed="false">' + c["edited"] + "</button>"
    gallery = [{**g, "image": asset(g["image"])} for g in c["gallery"]]
    steps = "".join('<article class="step"><div class="step-number"><span>0' + str(i + 1) + "</span>" + icon(["video", "cut", "download"][i]) + "</div><h3>" + escape(s[0]) + "</h3><p>" + escape(s[1]) + "</p></article>" for i, s in enumerate(c["steps"]))
    tabs = "".join('<button id="gallery-tab-' + str(i) + '" type="button" role="tab" aria-controls="gallery-panel" aria-selected="' + ("true" if i == 0 else "false") + '" tabindex="' + ("0" if i == 0 else "-1") + '" data-gallery="' + str(i) + '"><span class="num">0' + str(i + 1) + "</span>" + escape(g["label"]) + "</button>" for i, g in enumerate(gallery))
    install = "".join('<article class="install-step"><span>0' + str(i + 1) + "</span><div><h3>" + escape(s[0]) + "</h3><p>" + escape(s[1]) + '</p>' + ('<div class="code-row"><code id="install-command">brew install ffmpeg</code><button class="copy-button" type="button" aria-label="' + c["copy"] + '">' + icon("copy") + "</button></div>" if i == 1 else "") + "</div></article>" for i, s in enumerate(c["install"]))
    faqs = "".join('<details class="faq-item"><summary>' + escape(q) + "</summary><p>" + escape(a) + "</p></details>" for q, a in c["faq"])
    privacy_rows = "".join('<div class="privacy-row"><span>' + icon(["video", "sound", "spark"][i]) + escape(r[0]) + "</span><strong>" + escape(r[1]) + "</strong></div>" for i, r in enumerate(c["privacyRows"]))
    badges = "".join("<span>" + icon(["check", "lock", "cut"][i]) + escape(t) + "</span>" for i, t in enumerate(c["badges"]))
    legends = "".join('<span><i></i>' + escape(t) + "</span>" for t in c["legend"])
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f7f7f3">
<title>{escape(c["title"])}</title>
<meta name="description" content="{escape(c["description"], quote=True)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{escape(c["title"], quote=True)}">
<meta property="og:description" content="{escape(c["description"], quote=True)}">
<meta property="og:locale" content="{'tr_TR' if lang == 'tr' else 'en_US'}">
<meta name="twitter:card" content="summary">
<link rel="icon" type="image/svg+xml" href="{asset("logo.svg")}">
<link rel="stylesheet" href="{p}styles.css">
<script src="{p}script.js" defer></script>
</head>
<body>
<a class="skip" href="#main">{c["skip"]}</a>
<div class="wrap">
<header class="site-header">
<a class="brand" href="#main" aria-label="NU AI Video Editor"><img src="{asset("logo.svg")}" alt="" width="37" height="37"><span>NU AI<small>Video Editor</small></span></a>
<nav class="nav" id="main-nav" aria-label="{'Ana menü' if lang == 'tr' else 'Main navigation'}"><a href="#how-it-works">{c["nav"][0]}</a><a href="#features">{c["nav"][1]}</a><a href="#faq">{c["nav"][2]}</a></nav>
<div class="header-actions">
<div class="lang-switch" aria-label="{'Sayfa dili' if lang == 'tr' else 'Page language'}"><a href="{tr_url}" lang="tr" hreflang="tr" class="{'active' if lang == 'tr' else ''}" {'aria-current="page"' if lang == 'tr' else ''}>TR</a><span aria-hidden="true"></span><a href="{en_url}" lang="en" hreflang="en" class="{'active' if lang == 'en' else ''}" {'aria-current="page"' if lang == 'en' else ''}>EN</a></div>
{link(c["download"], "button small")}
<button class="menu-toggle" type="button" aria-label="{c["menu"]}" aria-controls="main-nav" aria-expanded="false">{icon("menu")}</button>
</div>
</header></div>
<main id="main"><div class="wrap">
<section class="hero" aria-labelledby="hero-title">
<div class="eyebrow"><span class="dot"></span>{c["eyebrow"]}</div>
<div class="hero-copy">
<h1 id="hero-title">{c["headline"]}</h1>
<div class="hero-side"><p class="hero-description">{c["intro"]}</p><div class="hero-actions">{link(c["downloadFree"])}<a class="text-link" href="#demo" data-show-demo>{c["seeDemo"]}{icon("arrow")}</a></div><p class="download-meta">{c["meta"]}</p></div>
</div>
<div class="hero-badges">{badges}</div>
<div class="studio" id="demo">
<div class="studio-top"><div class="window-dots" aria-hidden="true"><i></i><i></i><i></i></div><span class="studio-file">{icon("video")}studio_take_01.mp4</span><div class="studio-mode" role="group" aria-label="{c["sample"]}">{mode_buttons}</div></div>
<div class="studio-main">
<div class="scene">{SCENE}<span class="scene-label"><i></i>{c["sceneLabel"]}</span><span class="scene-corner">00:12 / 00:30</span><div class="scene-caption"><span>{c["caption"]}</span></div></div>
<div class="transcript"><div class="transcript-head"><span>{c["transcriptLabel"]}</span><span id="demo-state">{c["beforeState"]}</span></div><div class="transcript-content">{c["sentence"]}</div><div class="transcript-legend">{legends}</div></div>
</div>
<div class="timeline"><div class="timeline-meta"><span>{c["timeline"]}</span><strong id="demo-result">{c["beforeResult"]}</strong></div><div class="waveform"><svg viewBox="0 0 1075 43" preserveAspectRatio="none" aria-hidden="true" id="wave-bars"></svg><span class="cut-zone one"></span><span class="cut-zone two"></span><span class="cut-zone three"></span><span class="playhead"></span></div><div class="timeline-ticks" aria-hidden="true"><span>00:00</span><span>00:05</span><span>00:10</span><span>00:15</span><span>00:20</span><span>00:25</span><span>00:30</span></div><div class="mobile-demo-controls studio-mode" role="group" aria-label="{c["sample"]}">{mode_buttons}</div></div>
</div>
<div class="demo-foot"><span>{icon("file")}{c["demoNote"]}</span><span>{c["demoRight"]}</span></div>
</section>
<section class="section" id="how-it-works" aria-labelledby="flow-title"><div class="flow-intro"><div><div class="eyebrow"><span class="dot"></span>{c["flowEyebrow"]}</div><h2 class="section-title" id="flow-title">{c["flowTitle"]}</h2></div><p class="section-lead">{c["flowLead"]}</p></div><div class="steps">{steps}</div></section>
<section class="section" id="features" aria-labelledby="features-title"><div class="product-heading"><div><div class="eyebrow"><span class="dot"></span>{c["featuresEyebrow"]}</div><h2 class="section-title" id="features-title">{c["featuresTitle"]}</h2></div><p class="section-lead">{c["featuresLead"]}</p></div><div class="product-tabs" role="tablist" aria-label="{c["nav"][1]}">{tabs}</div><div id="gallery-panel" role="tabpanel" aria-labelledby="gallery-tab-0"><button class="screen-frame" type="button" aria-label="{c["expand"]}"><img id="product-screenshot" src="{gallery[0]["image"]}" alt="{escape(gallery[0]["alt"], quote=True)}" width="2880" height="1800" loading="lazy"><span class="screen-expand">{icon("expand")}{c["expand"]}</span></button><div class="screen-note"><h3 id="gallery-title">{gallery[0]["title"]}</h3><p id="gallery-description">{gallery[0]["description"]}</p></div></div></section>
</div>
<section class="privacy" aria-labelledby="privacy-title"><div class="wrap"><div><div class="eyebrow"><span class="dot"></span>{c["privacyEyebrow"]}</div><h2 class="section-title" id="privacy-title">{c["privacyTitle"]}</h2><p>{c["privacyBody"]}</p></div><div><div class="privacy-list">{privacy_rows}</div><p class="privacy-foot">{c["privacyFoot"]}</p></div></div></section>
<div class="wrap">
<section class="download-section" id="download" aria-labelledby="download-title"><div class="download-layout"><div class="download-copy"><div class="eyebrow"><span class="dot"></span>{c["downloadEyebrow"]}</div><h2 class="section-title" id="download-title">{c["downloadTitle"]}</h2><p class="section-lead">{c["downloadIntro"]}</p><div class="download-card"><img src="{asset("logo.svg")}" alt="" width="72" height="72"><div><strong>NU AI Video Editor</strong><span>{c["appMeta"]}</span></div></div>{link(c["downloadFree"])}<a class="release-link" href="{REPO}/releases/tag/v0.1.0" target="_blank" rel="noopener noreferrer">{c["release"]}{icon("arrow")}</a></div><div><div class="install-steps">{install}</div><p class="install-note">{c["installNote"]}</p></div></div></section>
<section class="section" id="faq" aria-labelledby="faq-title"><div class="faq-layout"><div><div class="eyebrow"><span class="dot"></span>{c["faqEyebrow"]}</div><h2 class="section-title" id="faq-title">{c["faqTitle"]}</h2></div><div class="faq-list">{faqs}</div></div></section>
<section class="final-cta" aria-labelledby="final-title"><a class="brand" href="#main"><img src="{asset("logo.svg")}" alt="" width="37" height="37">NU AI</a><h2 id="final-title">{c["finalTitle"]}</h2>{link(c["downloadFree"])}<p class="download-meta">{c["meta"]}</p></section>
</div></main><div class="wrap">
<footer class="footer"><div class="footer-brand">NU AI Video Editor<span>{c["footerLicense"]}</span></div><div class="footer-links"><a href="{REPO}" target="_blank" rel="noopener noreferrer">{c["footerLinks"][0]}</a><a href="{REPO}/issues" target="_blank" rel="noopener noreferrer">{c["footerLinks"][1]}</a><a href="{REPO}/releases" target="_blank" rel="noopener noreferrer">{c["footerLinks"][2]}</a></div></footer>
</div>
<dialog class="lightbox" id="screenshot-dialog" aria-labelledby="lightbox-title"><button class="lightbox-close" type="button">{c["close"]} ×</button><div class="lightbox-top"><span id="lightbox-title">{gallery[0]["label"]}</span><span>NU AI Video Editor</span></div><img id="lightbox-image" src="{gallery[0]["image"]}" alt="{escape(gallery[0]["alt"], quote=True)}" width="2880" height="1800"></dialog>
<div class="status-announcement" role="status" aria-live="polite" id="announcement"></div>
<script type="application/json" id="demo-copy">{json.dumps({k: c[k] for k in ["beforeState", "afterState", "beforeResult", "afterResult", "copied", "selectCommand"]}, ensure_ascii=False)}</script>
<script type="application/json" id="gallery-copy">{json.dumps(gallery, ensure_ascii=False)}</script>
</body></html>
"""

if __name__ == "__main__":
    for language in CONTENT:
        dest = ROOT / ("index.html" if language == "tr" else "en/index.html")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(generate(language), encoding="utf-8")
        print("Generated", dest.relative_to(ROOT))
