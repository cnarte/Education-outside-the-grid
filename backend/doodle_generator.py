import spacy_universal_sentence_encoder
from quickdraw import QuickDrawData
nlp = spacy_universal_sentence_encoder.load_model('en_use_lg')
qd = QuickDrawData()
from quickdraw import QuickDrawDataGroup

def doodle(text):
    doc_1 = nlp(text)
    score = {}
    for a in list(qd.drawing_names):
        doc_2 = nlp(a)
        score[a] = doc_1.similarity(doc_2)
    cat = sorted(score)
    doodle_cat = cat[0]
    ants = QuickDrawDataGroup(doodle_cat)
    ant = ants.get_drawing()
    ant.image.save("frontend/src/assets/doodle/doodle.jpg")

doodle("dog running ground")