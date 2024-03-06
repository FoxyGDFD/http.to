from django.views import View
from django.shortcuts import render

class CaratView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/carat.html', { 
            'title': 'Carat',
            'page_title': 'CARAT',
            'card': '<b>Вес драгоценного камня по разному влияет на стоимость камней.</b> \
                <ol><li>Первая группа. Стоимость растет в геометрической прогрессии.</li><li>Вторая группа. Стоимость растет в арифметической прогрессии. Стоимость возрастает пока вес камня не достигнет веса, после которого камень сложно использовать в ювелирном деле (крупные камни из этой группы пререходят на рынок коллекционеров).</li></ol> \
                <p>Каждый камень имеет свой предел, встречающегося в природе веса. Поэтому шаг возрастания цены для множества камней будет отличаться. Например. Разница стоимости 1 каратного аметиста и 3 каратного аметиста, будет намного меньше стоимости 1 каратного рубина и 3 каратного рубина.</p> \
                <p>Ниже мы приводим обобщенные данные о весе камня и примерное описание зависимости веса к стоимости.</p>',
            'list': [
                'Afghanite',
                'Aquamarine 0.2 - 50 ct',
                'Alexandrite 0.1 - 5 ct. Первая группа',
                'Amblygonite  0.25 - 22 ct',
                ] 
            })


class FreeVygemView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/free-vygem.html', { 'title': 'Vygem', 'page_title': '' })


class CutView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/cut.html', { 
            'title': 'Cut',
            'page_title': 'CUT',
            'main_card': "Качество огранки. \
                <br>Осматривается драгоценный камень через 10х лупу. При этом оцениваются пропорции и полировка камня. \
                При оценке пропорций учитывается красота и привлекательность камня. Состояние поверхности характеризуется наличием дефектов, обусловленных качеством обработки. Цветные драгоценные камни могут иметь как фасетную огранку, так и огранку в виде кабошона. Качество огранки и пропорции камня важны по следующим причинам: \
                <ul><li>влияют на глубину цвета камня;</li><li>влияют на игру и живость камня</li></ul>",
            'cards': [
                    "Excellent cut: optimal angles of the crown and pavilion facets, correct orientation of anisotropic material, optimal proportions of linear dimensions, good facet junctions, excellent polish, uniformity of the girdle within the norms.",
                    "Good cut: proper symmetry, reasonably correct proportions of linear and angular parameters, slight surface distortions, uniformity of the girdle within norms, surface with minor scratches and tool marks despite fairly good polish. Microscopic feathers may be concentrated on the girdle, barely discernible to the naked eye but easily seen under tenfold magnification.",
                    "Fair cut: noticeable cut flaws, easily visible to the naked eye, deviation from proper geometric forms, lack of parallelism between table and girdle facets, minor deviations in angular parameters, surface distortion, irregularity of the girdle within norms, scratches, girdle chips up to 0.2 mm in size, poor polish.",
                    "Poor cut - significant cut flaws, visible to the naked eye, asymmetrical facet arrangements, severe proportion deviations, significant surface distortion, lack of parallelism between table and girdle, major chips and scratches. Poor polish."
                ]
            })


class TransparencyView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/transparency.html', { 
            'title': 'Ttransparency',
            'page_title': 'TRANSPARENCY',
            'card': 'Transparency is understood as the ability of a solid substance to allow light rays to pass through to some degree. The transparency depends on the structure of the crystals, the presence of cracks, solid and gas-liquid inclusions, which hinder the passage of light through the stone. Transparency is visually determined by viewing the stone in transmitted light. Gemstones are classified by their transparency level as follows: \
                <ul><li>Transparent: all colorless and lightly colored gemstones, through which objects are clearly visible when viewed through plates (3-5 mm thick);</li><li>Translucent: gemstones through which objects are somewhat visible but not clearly;</li><li>Translucent: gemstones through which objects are not clearly visible;</li><li>Opaque: gemstones through which no light passes through.</li></ul> \
                The degree of transparency, namely the values ​​of the transparency coefficient and the absorption coefficient, can be determined quantitatively using spectrophotometers.' })
