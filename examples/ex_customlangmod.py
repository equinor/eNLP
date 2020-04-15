"""
Custom Spacy Language Models
============================
The following example illustrates how to generate word vectors from a corpus, save them to file and also generate
a custom spacy language model with them.


"""
import enlp.language_models as lm
import enlp.understanding.vectors as vts
import enlp.processing.stdtools as stdt


###############################################################################
# Load previously computed word vectors
wvs = vts.load_vectors('example_data/ex_wordvecs.bin', binary=True)

###############################################################################
# Create new language models with word vectors included
lang_mod = lm.add_vectors_to_langmod(wvs, 'en')


###############################################################################
# Proof that the new model works same as any other spacy language model

text = 'This is a test to check model is not crazy'

print ('Original: ', text)
print ('Processed: ', stdt.spacy_lemmatize(lang_mod, text))


###############################################################################
# Save new language model to be used in future work
mod_path = 'example_data/tmp_lang_mod/'
lm.save_spacy_model(lang_mod, mod_path)


###############################################################################
# To load this language model in future you can use:

import spacy
spacy.load(mod_path)
