# TEST.py
import os
import glob
import math
import ROOT
from ROOT import *
import sys
from AnaStep import *

lumi = 1

q1 	= "../trees/store/QCD/QCD_semilep.root"
Q1	= dist(q1, 'TEST', kRed, 19.55/1357312, "no")
Q2	= dist(q1, 'TEEFD', kGreen, 1, "yes")


STEPONE = pile("tree")
STEPONE.addSig(Q1)
STEPONE.addBkg(Q2)


# add cuts
cut0 = cut('jet1mass>130&jet1tau32<0.55&jet1tau32>0.0', 'event reco')
cut2 = cut('isMuon>0', 'mu')

STEPONE.addCut(cut0)
STEPONE.addCut(cut2)

TakeTheStep = AnaStep('test', STEPONE, lumi, 'jet1mass', [300,0,300], "no")

