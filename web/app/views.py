from django.views import View
from django.shortcuts import render


class MainView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/main.html', { 
            'title': 'Vygem',
            })


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


class ColorView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/color.html', { 
            'title': 'Color',
            'page_title': 'COLOR',
            'card': "<p>Color is the most important characteristic when evaluating a gemstone.</p> \
                <p>Our team has developed a methodology for determining the color of a gemstone based on computer and spectral color analysis. The essence of the methodology lies in determining the percentage of the base color hue and based on the data obtained, we propose to determine the color grading coefficient.</p> \
                <p>Our application utilizes the following methodology to determine the value of a gemstone based on its color. We take 32 basic color hues used by the GIA. For each basic hue, we have compiled a table representing a 'plane' where the abscissa represents 'Saturation', determining how pure and neutral the color of the stone is, and the ordinate represents 'Brightness', determining the intensity of the color from light to dark. At each coordinate point in our color table, the color contains a certain amount of the base color hue in percentage. For example, for the color hue 'R (Red)', the first point 1/1 will contain almost 100% red color. And the second point 2/4 will contain approximately 72% red color. Therefore, the value of a stone with a color matching the second point will be the value of the first point multiplied by 0.72. However, this does not apply to the entire table. Once the amount of the base color crosses the 50% threshold and the base color starts to 'fade', we add an additional discount coefficient to the stone value.</p> \
                <p>For example:<br> \
                Vivid/Medium (6/5) will have a coefficient of 1.<br> \
                Vivid/Light (6/3) will have a coefficient of 0.7<br> \
                Moderately strong/Medium light (4/4) will have a coefficient of 0.65<br></p> \
                <p>Using the example of the color table for the Red color hue presented below, the 'points of contact' between the VYGEM color methodology and the GIA color system are illustrated.</p>",
            })
    
class ColorView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/color.html', { 
            'title': 'Color',
            'page_title': 'COLOR',
            'card': "<p>Color is the most important characteristic when evaluating a gemstone.</p> \
                <p>Our team has developed a methodology for determining the color of a gemstone based on computer and spectral color analysis. The essence of the methodology lies in determining the percentage of the base color hue and based on the data obtained, we propose to determine the color grading coefficient.</p> \
                <p>Our application utilizes the following methodology to determine the value of a gemstone based on its color. We take 32 basic color hues used by the GIA. For each basic hue, we have compiled a table representing a 'plane' where the abscissa represents 'Saturation', determining how pure and neutral the color of the stone is, and the ordinate represents 'Brightness', determining the intensity of the color from light to dark. At each coordinate point in our color table, the color contains a certain amount of the base color hue in percentage. For example, for the color hue 'R (Red)', the first point 1/1 will contain almost 100% red color. And the second point 2/4 will contain approximately 72% red color. Therefore, the value of a stone with a color matching the second point will be the value of the first point multiplied by 0.72. However, this does not apply to the entire table. Once the amount of the base color crosses the 50% threshold and the base color starts to 'fade', we add an additional discount coefficient to the stone value.</p> \
                <p>For example:<br> \
                Vivid/Medium (6/5) will have a coefficient of 1.<br> \
                Vivid/Light (6/3) will have a coefficient of 0.7<br> \
                Moderately strong/Medium light (4/4) will have a coefficient of 0.65<br></p> \
                <p>Using the example of the color table for the Red color hue presented below, the 'points of contact' between the VYGEM color methodology and the GIA color system are illustrated.</p>",
            })
    

class ClarityView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/clarity.html', { 
            'title': 'CLARITY',
            'page_title': 'CLARITY',
            'card': "<p>Степень чистоты камня указывает на отсутствие включений, трещин, пятен и других дефектов, которые влияют на внешний вид и целостность камня. Камни делятся на три группы чистоты. К разной группе чистоты предъявляются разные требования. <br><br>Флуорисценция - свечение вокруг камня. У некоторых камней с одного месторождения есть свечение с другого нет. Разница в цене огромная</p>",
            })
    

class GemsNameView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/gems-name.html', { 
            'title': 'GEMS NAME',
            'page_title': 'GEMS NAME',
            'card': "<p>Для корректного определения стоимости вашего камня необходима его идентификация.  Множество камней могут иметь одинаковый цвет и визуально одинаковые внешние параметры. К сожалению, мы не всегда можем положится на данные указанные на ярлыке ювелирного магазина в котором был приобретен  драгоценный камень. Окончательное заключение может дать только опытный геммолог. Однако и с геммологами и геммологическими лабораториями не все однозначно. например: Некоторые лаборатории могут назвать камень рубином, в то время как другие могут назвать его розовым сапфиром. Цена рубина будет в несколько раз больше цены сапфира.<br><br>Мы убедительно просим Вас не очаровываться вашим драгоценным камнем до того момента пока его стоимость и уникальность не будет подтверждена специалистами. Мы искренне не хотим, что бы Вы испытали разочарование узнав о том, что Ваш “самый лучший камень на Земле” оказывается рядовым камнем и что хуже имитацией или подделкой</p>",
            })