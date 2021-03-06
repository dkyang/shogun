#!/usr/bin/env python
from tools.load import LoadMatrix
from numpy import random
lm=LoadMatrix()

try:
	from shogun.Evaluation import DirectorContingencyTableEvaluation, ED_MAXIMIZE
except ImportError:
	print "recompile shogun with --enable-swig-directors"
	import sys
	sys.exit(0)

class SimpleWeightedBinaryEvaluator(DirectorContingencyTableEvaluation):
	def __init__(self):
		DirectorContingencyTableEvaluation.__init__(self)
	def get_custom_direction(self):
		return ED_MAXIMIZE
	def get_custom_score(self):
		return self.get_WRACC()+self.get_BAL()

ground_truth = lm.load_labels('../data/label_train_twoclass.dat')
random.seed(17)
predicted = random.randn(len(ground_truth))

parameter_list = [[ground_truth,predicted]]

def evaluation_director_contingencytableevaluation_modular (ground_truth, predicted):
	from shogun.Features import BinaryLabels

	evaluator = SimpleWeightedBinaryEvaluator()
	r = evaluator.evaluate(BinaryLabels(ground_truth), BinaryLabels(predicted))
	r2 = evaluator.get_custom_score()

	return r==r2

if __name__=='__main__':
	print('EvaluationDirectorContingencyTableEvaluation')
	evaluation_director_contingencytableevaluation_modular(*parameter_list[0])

