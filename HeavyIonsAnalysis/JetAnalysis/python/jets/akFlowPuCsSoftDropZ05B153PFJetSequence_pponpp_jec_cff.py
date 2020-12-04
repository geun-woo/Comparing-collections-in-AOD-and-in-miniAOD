import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akFlowPuCsSoftDropZ05B153PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B153PFJets"),
    matched = cms.InputTag("ak3GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akFlowPuCsSoftDropZ05B153PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B153GenJets"),
    matched = cms.InputTag("ak3GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akFlowPuCsSoftDropZ05B153PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B153PFJets"),
    matched = cms.InputTag("genParticles"))

akFlowPuCsSoftDropZ05B153PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akFlowPuCsSoftDropZ05B153PFJets"),
    payload = "AK3PF"
    )

akFlowPuCsSoftDropZ05B153PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akFlowPuCsSoftDropZ05B153CaloJets'))

# akFlowPuCsSoftDropZ05B153PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak3GenJets'))

akFlowPuCsSoftDropZ05B153PFbTagger = bTaggers(
    "akFlowPuCsSoftDropZ05B153PF",
    0.3)

# create objects locally since they dont load properly otherwise
akFlowPuCsSoftDropZ05B153PFPatJetFlavourAssociationLegacy = akFlowPuCsSoftDropZ05B153PFbTagger.PatJetFlavourAssociationLegacy
akFlowPuCsSoftDropZ05B153PFPatJetPartons = akFlowPuCsSoftDropZ05B153PFbTagger.PatJetPartons
akFlowPuCsSoftDropZ05B153PFJetTracksAssociatorAtVertex = akFlowPuCsSoftDropZ05B153PFbTagger.JetTracksAssociatorAtVertex
akFlowPuCsSoftDropZ05B153PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akFlowPuCsSoftDropZ05B153PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B153PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B153PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B153PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.CombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDropZ05B153PFJetBProbabilityBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.JetBProbabilityBJetTags
akFlowPuCsSoftDropZ05B153PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B153PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDropZ05B153PFTrackCountingHighEffBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.TrackCountingHighEffBJetTags
akFlowPuCsSoftDropZ05B153PFTrackCountingHighPurBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.TrackCountingHighPurBJetTags
akFlowPuCsSoftDropZ05B153PFPatJetPartonAssociationLegacy = akFlowPuCsSoftDropZ05B153PFbTagger.PatJetPartonAssociationLegacy
akFlowPuCsSoftDropZ05B153PFPatJetPartonAssociationLegacy.partons = "myPartons"

akFlowPuCsSoftDropZ05B153PFImpactParameterTagInfos = akFlowPuCsSoftDropZ05B153PFbTagger.ImpactParameterTagInfos
akFlowPuCsSoftDropZ05B153PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDropZ05B153PFJetProbabilityBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.JetProbabilityBJetTags

akFlowPuCsSoftDropZ05B153PFSecondaryVertexTagInfos = akFlowPuCsSoftDropZ05B153PFbTagger.SecondaryVertexTagInfos
akFlowPuCsSoftDropZ05B153PFSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B153PFSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B153PFCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.CombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B153PFCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.CombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDropZ05B153PFSecondaryVertexNegativeTagInfos = akFlowPuCsSoftDropZ05B153PFbTagger.SecondaryVertexNegativeTagInfos
akFlowPuCsSoftDropZ05B153PFNegativeSimpleSecondaryVertexHighEffBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akFlowPuCsSoftDropZ05B153PFNegativeSimpleSecondaryVertexHighPurBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akFlowPuCsSoftDropZ05B153PFNegativeCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B153PFPositiveCombinedSecondaryVertexBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akFlowPuCsSoftDropZ05B153PFNegativeCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akFlowPuCsSoftDropZ05B153PFPositiveCombinedSecondaryVertexV2BJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akFlowPuCsSoftDropZ05B153PFSoftPFMuonsTagInfos = akFlowPuCsSoftDropZ05B153PFbTagger.SoftPFMuonsTagInfos
akFlowPuCsSoftDropZ05B153PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akFlowPuCsSoftDropZ05B153PFSoftPFMuonBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.SoftPFMuonBJetTags
akFlowPuCsSoftDropZ05B153PFSoftPFMuonByIP3dBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.SoftPFMuonByIP3dBJetTags
akFlowPuCsSoftDropZ05B153PFSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.SoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B153PFNegativeSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.NegativeSoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B153PFPositiveSoftPFMuonByPtBJetTags = akFlowPuCsSoftDropZ05B153PFbTagger.PositiveSoftPFMuonByPtBJetTags
akFlowPuCsSoftDropZ05B153PFPatJetFlavourIdLegacy = cms.Sequence(akFlowPuCsSoftDropZ05B153PFPatJetPartonAssociationLegacy*akFlowPuCsSoftDropZ05B153PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akFlowPuCsSoftDropZ05B153PFPatJetFlavourAssociation = akFlowPuCsSoftDropZ05B153PFbTagger.PatJetFlavourAssociation
# akFlowPuCsSoftDropZ05B153PFPatJetFlavourId = cms.Sequence(akFlowPuCsSoftDropZ05B153PFPatJetPartons*akFlowPuCsSoftDropZ05B153PFPatJetFlavourAssociation)

akFlowPuCsSoftDropZ05B153PFJetBtaggingIP = cms.Sequence(
    akFlowPuCsSoftDropZ05B153PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B153PFTrackCountingHighEffBJetTags +
    akFlowPuCsSoftDropZ05B153PFTrackCountingHighPurBJetTags +
    akFlowPuCsSoftDropZ05B153PFJetProbabilityBJetTags +
    akFlowPuCsSoftDropZ05B153PFJetBProbabilityBJetTags
    )

akFlowPuCsSoftDropZ05B153PFJetBtaggingSV = cms.Sequence(
    akFlowPuCsSoftDropZ05B153PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B153PFSecondaryVertexTagInfos *
    akFlowPuCsSoftDropZ05B153PFSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDropZ05B153PFSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDropZ05B153PFCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B153PFCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDropZ05B153PFJetBtaggingNegSV = cms.Sequence(
    akFlowPuCsSoftDropZ05B153PFImpactParameterTagInfos *
    akFlowPuCsSoftDropZ05B153PFSecondaryVertexNegativeTagInfos *
    akFlowPuCsSoftDropZ05B153PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akFlowPuCsSoftDropZ05B153PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akFlowPuCsSoftDropZ05B153PFNegativeCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B153PFPositiveCombinedSecondaryVertexBJetTags +
    akFlowPuCsSoftDropZ05B153PFNegativeCombinedSecondaryVertexV2BJetTags +
    akFlowPuCsSoftDropZ05B153PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akFlowPuCsSoftDropZ05B153PFJetBtaggingMu = cms.Sequence(
    akFlowPuCsSoftDropZ05B153PFSoftPFMuonsTagInfos *
    akFlowPuCsSoftDropZ05B153PFSoftPFMuonBJetTags +
    akFlowPuCsSoftDropZ05B153PFSoftPFMuonByIP3dBJetTags +
    akFlowPuCsSoftDropZ05B153PFSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDropZ05B153PFNegativeSoftPFMuonByPtBJetTags +
    akFlowPuCsSoftDropZ05B153PFPositiveSoftPFMuonByPtBJetTags
    )

akFlowPuCsSoftDropZ05B153PFJetBtagging = cms.Sequence(
    akFlowPuCsSoftDropZ05B153PFJetBtaggingIP
    * akFlowPuCsSoftDropZ05B153PFJetBtaggingSV
    # * akFlowPuCsSoftDropZ05B153PFJetBtaggingNegSV
    # * akFlowPuCsSoftDropZ05B153PFJetBtaggingMu
    )

akFlowPuCsSoftDropZ05B153PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akFlowPuCsSoftDropZ05B153PFJets"),
    genJetMatch            = cms.InputTag("akFlowPuCsSoftDropZ05B153PFmatch"),
    genPartonMatch         = cms.InputTag("akFlowPuCsSoftDropZ05B153PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDropZ05B153PFcorr")),
    JetPartonMapSource     = cms.InputTag("akFlowPuCsSoftDropZ05B153PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akFlowPuCsSoftDropZ05B153PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akFlowPuCsSoftDropZ05B153PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akFlowPuCsSoftDropZ05B153PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B153PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B153PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B153PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B153PFJetBProbabilityBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B153PFJetProbabilityBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDropZ05B153PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akFlowPuCsSoftDropZ05B153PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B153PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akFlowPuCsSoftDropZ05B153PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akFlowPuCsSoftDropZ05B153PFImpactParameterTagInfos"),cms.InputTag("akFlowPuCsSoftDropZ05B153PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akFlowPuCsSoftDropZ05B153PFJetID"),
    addBTagInfo = True,
    addTagInfos = True,
    addDiscriminators = True,
    addAssociatedTracks = True,
    addJetCharge = False,
    addJetID = False,
    getJetMCFlavour = True,
    addGenPartonMatch = True,
    addGenJetMatch = True,
    embedGenJetMatch = True,
    embedGenPartonMatch = True,
    # embedCaloTowers = False,
    # embedPFCandidates = True
    )

akFlowPuCsSoftDropZ05B153PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akFlowPuCsSoftDropZ05B153PFJets"),
    R0  = cms.double(0.3)
    )

akFlowPuCsSoftDropZ05B153PFpatJetsWithBtagging.userData.userFloats.src += [
    'akFlowPuCsSoftDropZ05B153PFNjettiness:tau1',
    'akFlowPuCsSoftDropZ05B153PFNjettiness:tau2',
    'akFlowPuCsSoftDropZ05B153PFNjettiness:tau3']

akFlowPuCsSoftDropZ05B153PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akFlowPuCsSoftDropZ05B153PFpatJetsWithBtagging"),
    genjetTag = 'ak3GenJets',
    rParam = 0.3,
    matchJets = cms.untracked.bool(False),
    matchTag = 'patJetsWithBtagging',
    pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
    trackTag = cms.InputTag("generalTracks"),
    fillGenJets = True,
    isMC = True,
    doSubEvent = True,
    useHepMC = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    eventInfoTag = cms.InputTag("generator"),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    bTagJetName = cms.untracked.string("akFlowPuCsSoftDropZ05B153PF"),
    jetName = cms.untracked.string("akFlowPuCsSoftDropZ05B153PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B153GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDropZ05B153GenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDropZ05B153GenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDropZ05B153GenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDropZ05B153GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDropZ05B153GenJets","droppedBranches")
    )

akFlowPuCsSoftDropZ05B153PFJetSequence_mc = cms.Sequence(
    # akFlowPuCsSoftDropZ05B153PFclean
    # *
    akFlowPuCsSoftDropZ05B153PFmatch
    # *
    # akFlowPuCsSoftDropZ05B153PFmatchGroomed
    *
    akFlowPuCsSoftDropZ05B153PFparton
    *
    akFlowPuCsSoftDropZ05B153PFcorr
    # *
    # akFlowPuCsSoftDropZ05B153PFJetID
    *
    akFlowPuCsSoftDropZ05B153PFPatJetFlavourIdLegacy
    # *
    # akFlowPuCsSoftDropZ05B153PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akFlowPuCsSoftDropZ05B153PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDropZ05B153PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akFlowPuCsSoftDropZ05B153PFNjettiness
    *
    akFlowPuCsSoftDropZ05B153PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDropZ05B153PFJetAnalyzer
    )

akFlowPuCsSoftDropZ05B153PFJetSequence_data = cms.Sequence(
    akFlowPuCsSoftDropZ05B153PFcorr
    *
    # akFlowPuCsSoftDropZ05B153PFJetID
    # *
    akFlowPuCsSoftDropZ05B153PFJetTracksAssociatorAtVertex
    *
    akFlowPuCsSoftDropZ05B153PFJetBtagging
    *
    akFlowPuCsSoftDropZ05B153PFNjettiness
    *
    akFlowPuCsSoftDropZ05B153PFpatJetsWithBtagging
    *
    akFlowPuCsSoftDropZ05B153PFJetAnalyzer
    )

akFlowPuCsSoftDropZ05B153PFJetSequence_mb = cms.Sequence(
    akFlowPuCsSoftDropZ05B153PFJetSequence_mc)
akFlowPuCsSoftDropZ05B153PFJetSequence_jec = cms.Sequence(
    akFlowPuCsSoftDropZ05B153PFJetSequence_mc)

akFlowPuCsSoftDropZ05B153PFJetSequence = cms.Sequence(
    akFlowPuCsSoftDropZ05B153PFJetSequence_jec)
akFlowPuCsSoftDropZ05B153PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akFlowPuCsSoftDropZ05B153PFJetAnalyzer.jetPtMin = cms.double(1)
akFlowPuCsSoftDropZ05B153PFpatJetsWithBtagging.userData.userFloats.src += ['akFlowPuCsSoftDropZ05B153PFJets:sym']
akFlowPuCsSoftDropZ05B153PFpatJetsWithBtagging.userData.userInts.src += ['akFlowPuCsSoftDropZ05B153PFJets:droppedBranches']
