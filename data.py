import json

data = {
    "questions": [
        {
            "question": "Okatmagyň we bilim bermegiň nazaryýeti haýsy sözde jemlenýär?",
            "variants": ("Metodika", "Pedagogika", "Dioletika"),
            "true": "3",
        },
        {
            "question": "Aidrogogika nähili pedagogikadyr?",
            "variants": (
                "Mekdebe çenli ýaşly çagalaryň pedogogikasy",
                "Uly ýaşly adamlaryň pedagogikasy",
                "Ýokary okuw jaýlarynyň pedagogikasy",
            ),
            "true": "2",
        },
        {
            "question": "Jenaýat endikleri üçin azatlykdan mahrum edilen adamlaryň saklanýan,\nolary gorkdan terbiýelemek bilen meşgullanýan pedagogika haýsy?",
            "variants": (
                "Düzediş-zähmet pedagogikasy",
                "Professional pedagogika",
                "Sosial pedagogika",
            ),
            "true": "1",
        },
        {
            "question": "Pedagogikanyň metodologiýasy haýsy wezipeleri/funksiýalary ýerine ýetirýär?",
            "variants": (
                "Tankydy, akyl ýetirmek refleksiýa",
                "Tankydy terbiýe okatmak",
                "Refleksiýa, akyl ýetirmek, bilim-terbiýe",
            ),
            "true": "3",
        },
        {
            "question": "Bilim maksatnamasy haýsy ugurlara bölünýär?",
            "variants": (
                "Umumy bilim, hünär bilim",
                "Umumy bilim, ýokary bilim",
                "Umumy orta bilim, ýokary bilim",
            ),
            "true": "3",
        },
        {
            "question": 'Ýokary hünär bilimi hakyndaky ähli maksatlary Türkmenistanyň "Bilim"\nhakynda kanunyň rejelenen görnüşiniň haýsy maddasynda berilendir?',
            "variants": (
                "24-nji madda",
                "28-nji madda",
                "55-nji madda",
            ),
            "true": "1",
        },
        {
            "question": "Indiwid kim?",
            "variants": (
                "Özbaşdak pikirlenip bilýän sosiallaşan adamlar we akyl taýdan yza galanlar",
                "Şahsyýet we 18 ýaşa çenli çagalar",
                "Köpüň biri, 18 ýaşa çenli çagalar we akyl taýdan yza galanlar",
            ),
            "true": "2",
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
            "question": "Şahsyýetiň kemala gelmegine täsir edýän humol däl subýektler haýsylar?",
            "variants": (
                "Gundeler, tanyşlar, erkin gatnaşyklar, sungat we medeniýet edebiýat",
                "Sosial gatlaklar, alymlar, bilim ulgamy",
                "Garyndaşlar, ene-atalar, ýokary bilimli adamlar",
            ),
            "true": "3",
        },
        {
            "question": "Prental ösüş näme?",
            "variants": (
                "Irki bäbeklik döwri",
                "Enäniň göwsündäki ösüş döwri",
                "Uly mekdep ýaşly çagalar",
            ),
            "true": "1",
        },
        {
            "question": "Şahsyýetiň esasan üç sany faktoryň nesle geçirijileriň sosial sredanyň\ntälim täsiri bilen kemala gelýändigini subut edýän alym kim?",
            "variants": (
                "Aristotel",
                "Platon",
                "L.P.Pawlow",
            ),
            "true": "3",
        },
        {
            "question": "Aksekrasiýa näme?",
            "variants": (
                "Adamyň beden ösüşiniň tizlenmegi",
                "Adamyň akyl taýdan ösüşiniň tizlenmegi",
                "Adamyň daş-töweregi bagly ösüşiniň tizlenmegi",
            ),
            "true": "1",
        },
        {
            "question": '"Terbiýe - bu çagalaryň ululara onsyz öýkenmesidir?" diýip alym belläpdir?',
            "variants": (
                "Monro",
                "A.Diskweg",
                "L.Tolstoý",
            ),
            "true": "3",
        },
        {
            "question": "Adamyň emosional lezzet alyş duýgysyny nähili terbiýe kämilleşdirýär?",
            "variants": (
                "Ahlak terbiýesi",
                "Gazetlik terbiýesi",
                "Zähmet terbiýesi",
            ),
            "true": "1",
        },
        {
            "question": '"Beýik didaktika" kimiň işi?',
            "variants": (
                "W.Roflu",
                "Ýa.A.Homenskiý",
                "A.S.Makaunko",
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
                "Mugallym bilen okuwçysyny aragatnaşygy",
            ),
            "true": "1",
        },
        {
            "question": "Indiwidual diýen düşünje nämäni aňladýar?",
            "variants": (
                "Häzirki zaman ösen adamzat jemgyýetini emele getiren umumylygyny aňladýar",
                "Özüňe derňemäge, özüňi bahalamaga, özüňe gözegçilik etmäge ukybyň bolmagy",
                "Kimdir biriniň gözegçiligine mätäç adamlar",
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
