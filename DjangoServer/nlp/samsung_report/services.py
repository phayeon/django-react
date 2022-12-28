
from dataclasses import dataclass
import nltk

from nlp.samsung_report.models import SamsungModel


@dataclass
class Entity:
    context: str
    fname: str
    target: str

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def target(self) -> str: return self._target

    @target.setter
    def target(self, target): self._target = target


class SamsungService:
    def __init__(self):
        self.entity = Entity()
        self.service = SamsungModel()

    def download_dictionary(self):
        nltk.download('all')

    def data_analysis(self):
        self.entity.fname = '\kr-Report_2018.txt'
        self.entity.context = r'C:\Users\AIA\PycharmProjects\django-react\DjangoServer\nlp\samsung_report\data'
        self.service.extract_tokens(self.entity)
        self.service.extract_hangeul()
        self.service.conversion_token()
        self.service.compound_noun()
        self.entity.fname = '\stopwords.txt'
        self.service.extract_stopword(self.entity)
        self.service.filtering_text_with_stopword()
        return self.service.frequent_text()
        # self.entity.fname = r'\D2Coding.ttf'
        # self.service.draw_wordcloud(self.entity)

if __name__ == '__main__':
    # app.download_dictionary()
    SamsungService().data_analysis()
