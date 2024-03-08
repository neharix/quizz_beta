import json

data = {
    "questions": [
        {
            "question": "Okatmagyň we bilim bermegiň nazaryýeti haýsy sözde jemlenýär?",
            "variants": ("Metodika", "Pedagogika", "Dioletika"),
            "true": "3",
        },
        {
            "question": "Androgogika nähili pedagogikadyr?",
            "variants": (
                "Mekdebe çenli ýaşly çagalaryň pedogogikasy",
                "Uly ýaşly adamlaryň pedagogikasy",
                "Ýokary okuw jaýlarynyň pedagogikasy",
            ),
            "true": "2",
        },
        {
            "question": "Jenaýat endikleri üçin azatlykdan mahrum edilen adamlaryň saklanýan,\nolary gaýtadan terbiýelemek bilen meşgullanýan pedagogika haýsy?",
            "variants": (
                "Düzediş-zähmet pedagogikasy",
                "Konfessional pedagogika",
                "Sosial pedagogika",
            ),
            "true": "1",
        },
        {
            "question": "Pedagogikanyň metodologiýasy haýsy wezipeleri(funksiýalary) ýerine ýetirýär?",
            "variants": (
                "Tankydy, akyl ýetirmek, refleksiýa",
                "Tankydy terbiýe okatmak",
                "Refleksiýa, akyl ýetirmek, bilim-terbiýe",
            ),
            "true": "1",
        },
        {
            "question": "Bilim maksatnamasy haýsy ugurlara bölünýär?",
            "variants": (
                "Umumy bilim, hünär bilim",
                "Umumy bilim, ýokary bilim",
                "Umumy orta bilim, ýokary bilim",
            ),
            "true": "1",
        },
        {
            "question": 'Ýokary hünär bilimi hakyndaky ähli maksatlary Türkmenistanyň "Bilim"\nhakynda kanunyň rejelenen görnüşiniň haýsy maddasynda berilendir?',
            "variants": (
                "24-nji madda",
                "28-nji madda",
                "55-nji madda",
            ),
            "true": "2",
        },
        {
            "question": "Indiwid kim?",
            "variants": (
                "Özbaşdak pikirlenip bilýän sosiallaşan adamlar we akyl taýdan yza galanlar",
                "Şahsyýet we 18 ýaşa çenli çagalar",
                "Köpüň biri, 18 ýaşa çenli çagalar we akyl taýdan yza galanlar",
            ),
            "true": "3",
        },
        {
            "question": "Adaptasiýa näme?",
            "variants": (
                "Duýgurlyk",
                "Uýgunlaşmak",
                "Öwrenişmek",
            ),
            "true": "2",
        },
        {
            "question": "Şahsyýetiň kemala gelmegine täsir edýän faktorlar haýsylar?",
            "variants": (
                "Terbiýe, nesle geçirijilik, sosial sreda",
                "Terbiýe, bilim, akyl-paýhas",
                "Terbiýe, biologik we fiziologik aýratynlyklary",
            ),
            "true": "1",
        },
        {
            "question": "Şahsyýetiň kemala gelmegine täsir edýän formal däl subýektler haýsylar?",
            "variants": (
                "Gurnaklar, tanyşlar, erkin gatnaşyklar, sungat we medeniýet edebiýat",
                "Sosial gatlaklar, alymlar, bilim ulgamy",
                "Garyndaşlar, ene-atalar, ýokary bilimli adamlar",
            ),
            "true": "1",
        },
        {
            "question": "Prental ösüş näme?",
            "variants": (
                "Irki bäbeklik döwri",
                "Enäniň göwsündäki ösüş döwri",
                "Uly mekdep ýaşly çagalar",
            ),
            "true": "2",
        },
        {
            "question": "Şahsyýetiň esasan üç sany faktoryň nesle geçirijiliginiň sosial sredanyň\ntälim terbiýäniň täsiri bilen kemala gelýändigini subut edýän alym kim?",
            "variants": (
                "Aristotel",
                "Platon",
                "L.P.Pawlow",
            ),
            "true": "3",
        },
        {
            "question": "Aksellerasiýa näme?",
            "variants": (
                "Adamyň beden ösüşiniň tizlenmegi",
                "Adamyň akyl taýdan ösüşiniň tizlenmegi",
                "Adamyň daş-töweregi bagly ösüşiniň tizlenmegi",
            ),
            "true": "1",
        },
        {
            "question": '"Terbiýe - bu çagalaryň ululara aňsyz öýkenmesidir?" diýip haýsy alym belläpdir?',
            "variants": (
                "Monro",
                "A.Diskweg",
                "L.Tolstoý",
            ),
            "true": "1",
        },
        {
            "question": "Adamyň emosional lezzet alyş duýgysyny nähili terbiýe kämilleşdirýär?",
            "variants": (
                "Ahlak terbiýesi",
                "Gözellik terbiýesi",
                "Zähmet terbiýesi",
            ),
            "true": "2",
        },
        {
            "question": '"Beýik didaktika" kimiň işi?',
            "variants": (
                "W.Ratke",
                "Ýa.A.Komenskiý",
                "A.S.Makarenko",
            ),
            "true": "2",
        },
        {
            "question": "Çaganyň kiçi mekdep ýaşly döwri näçe ýaşdan näçe ýaşa çenli?",
            "variants": (
                "7 ýaşdan 12 ýaşa çenli",
                "6 ýaşdan 11 ýaşa çenli",
                "8 ýaşdan 11 ýaşa çenli",
            ),
            "true": "2",
        },
        {
            "question": "Okatmagyň funksiýalary haýsylar?",
            "variants": (
                "Okatmak, jemgyýetde goşmak, sosiallaşdyrmak",
                "Okatmak, terbiýe bermek ösdürmek",
                "Okatmak, şahsyýet edip ýetişdirmek",
            ),
            "true": "2",
        },
        {
            "question": "Okatmak işi näme?",
            "variants": (
                "Bilim, ylym bermek",
                "Dersler bilen tanyşdyrmak",
                "Mugallym bilen okuwçynyň aragatnaşygy",
            ),
            "true": "3",
        },
        {
            "question": "Indiwid diýen düşünje nämäni aňladýar?",
            "variants": (
                "Häzirki zaman ösen adamzat jemgyýetini emele getiren umumylyklygyny aňladýar",
                "Özüňe derňemäge, özüňi bahalamaga, özüňe gözegçilik etmäge ukybyň bolmagy",
                "Kimdir biriniň gözegçiligine mätäç adamlar",
            ),
            "true": "3",
        },
        # continue
        {
            "question": "Türkmenistanyň Magtymguly adyndaky Ýaşlar guramasy haçan döredildi?",
            "variants": (
                "1994-nji ýylyň 15-nji oktýabry",
                "1994-nji ýylyň 15-nji noýabry",
                "1991-nji ýylyň 16-njy noýabry",
            ),
            "true": "1",
        },
        {
            "question": "Iholastika diýmek näme?",
            "variants": (
                "Alym-mekdep",
                "Dini mekdep",
                "Ýokary okuw",
            ),
            "true": "1",
        },
        {
            "question": '"Bilim hakynda" Türkmenistanyň kanunynyň rejelenen görnüşi\nnäçe maddadan durýar?',
            "variants": (
                "60",
                "12",
                "62",
            ),
            "true": "1",
        },
        {
            "question": "Diskusiýa görnüşi okatmagyň haýsy usulyna degişli?",
            "variants": (
                "Amaly usuly",
                "Görkezme usuly",
                "Söz üsti usuly",
            ),
            "true": "1",
        },
        {
            "question": "Pedagogiki garaýyşlarwe pikirler ýazuwyň döremeginden öň nämelerde\nýüze çykypdyr?",
            "variants": (
                "Aýdymlarda, yrymlarda, ýadygärliklerde",
                "Nakyllarda, yrymlarda, meklerde",
                "Mukaddes kitaplarda, rowaýatlarda, däp=dessurlarda, yrymlarda",
            ),
            "true": "1",
        },
        {
            "question": "Çaganyň ösüşinde ýaş aýratynlyklaryna bölmekde psihologik ösüş\nhaýsy ýagdaýlary öz içine alýar?",
            "variants": (
                "Ünsüň, pikirlenmäniň we sözleýşiň, temperamentiň we gylyk-häsiýetiň\n    aýratynlyklary degişlidir",
                "Gan-aýlanyş, içki mäzleriň, nerw sistemasynyň we ş.m. degişlidir",
                "Hyýala getirmeleriň, syýasy, ahlak garaýyşlarynyň nerw sistemasyny\n    we ş.m degişlidir",
            ),
            "true": "1",
        },
        {
            "question": "Pedagog sözi ilkibaşda nähili düşünjede ulanylypdyr?",
            "variants": (
                "Gadymy Gresiýada öz eýesiniň çagasynyň mekdebe äkidip getirýän\n    gula ýüzlenipdirler",
                "Afiny mekdeplerinde bilim berýän mugallymlara ýüzlenipdirler",
                "Halypa",
            ),
            "true": "1",
        },
        {
            "question": "Bilim bermekde dürli dersleri bilen baglanyşykda öwrenmekligi haýsy\nGündogar akyldary maslahat beripdir?",
            "variants": (
                "Al Horezmi",
                "Al Faraby",
                "Al Biruny",
            ),
            "true": "1",
        },
        {
            "question": "Didaktika sözüni ilkinji gezek ylmy dolanyşyga girizen alym kim?",
            "variants": (
                "Frensis Bekon",
                "Aristotel",
                "Ýan Amos Komenskiý",
            ),
            "true": "1",
        },
        {
            "question": "Bilimleri, başarnyklary, endikleri özleşdirmek hem-de emele getirmek\nmaksady bilen ýörite gurnalýan mugallymlaryň we okuwçylaryň aragatnaşygyna\nnäme diýilýär?",
            "variants": (
                "Okatmak",
                "Sosiallaşmak",
                "Terbiýelemek",
            ),
            "true": "1",
        },
        {
            "question": "Belli bir endigi, bilimi, başarnygy ýa-da okuw öwretmek we özleşdirmek\nüçin ýörite gurnalýan sapaklaryň gidişine näme diýilýär?",
            "variants": (
                "Guramaçylyk",
                "Okuw prosesi",
                "Pedagogik iş",
            ),
            "true": "1",
        },
        {
            "question": "Okatmagyň maksadyna we wezipelerine näme diýilýär?",
            "variants": (
                "Forma",
                "Metod",
                "Serişde",
            ),
            "true": "1",
        },
        {
            "question": "Okatmak döwrüniň kanunalaýyklygy netijesinde okuwçylara häzirki döwrüň\ntalabyna laýyk bilim we terbiýe kanun maksady bilen ulanylýan esasy\nbaş düzgünlere näme diýilýär?",
            "variants": (
                "Bilim bermek",
                "Okatmagyň esaslary",
                "Okatmagyň düzgünleri",
            ),
            "true": "1",
        },
        {
            "question": "Mugallymyň okuwçylara maglumatlary bermek, terbiýelemek, aňlaatmak we\ndurmuşda ulanmagyň maksadyny düşündirmek boýunça tertiplenen işe näme\ndiýilýär?",
            "variants": (
                "Okatmak",
                "Okamak",
                "Didaktika",
            ),
            "true": "1",
        },
    ]
}
new_data = json.dumps(data)
with open("quizz_data.json", "w+") as file:
    file.write(new_data)


# with open("quizz_data.json", "r") as file:
#             self.quizz_data = file.read()
#             self.quizz_data = json.loads(self.quizz_data)
