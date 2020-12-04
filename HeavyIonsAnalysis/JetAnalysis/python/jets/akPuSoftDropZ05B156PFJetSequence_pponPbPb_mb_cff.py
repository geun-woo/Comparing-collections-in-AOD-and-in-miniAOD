import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropZ05B156PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropZ05B156PFJets"),
    matched = cms.InputTag("ak6HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akPuSoftDropZ05B156PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropZ05B156HiGenJets"),
    matched = cms.InputTag("ak6HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akPuSoftDropZ05B156PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akPuSoftDropZ05B156PFJets"),
    matched = cms.InputTag("cleanedPartons"))

akPuSoftDropZ05B156PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akPuSoftDropZ05B156PFJets"),
    payload = "AK6PF"
    )

akPuSoftDropZ05B156PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akPuSoftDropZ05B156CaloJets'))

# akPuSoftDropZ05B156PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak6HiCleanedGenJets'))

akPuSoftDropZ05B156PFbTagger = bTaggers(
    "akPuSoftDropZ05B156PF",
    0.6)

# create objects locally since they dont load properly otherwise
akPuSoftDropZ05B156PFPatJetFlavourAssociationLegacy = akPuSoftDropZ05B156PFbTagger.PatJetFlavourAssociationLegacy
akPuSoftDropZ05B156PFPatJetPartons = akPuSoftDropZ05B156PFbTagger.PatJetPartons
akPuSoftDropZ05B156PFJetTracksAssociatorAtVertex = akPuSoftDropZ05B156PFbTagger.JetTracksAssociatorAtVertex
akPuSoftDropZ05B156PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B156PFCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B156PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B156PFbTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropZ05B156PFJetBProbabilityBJetTags = akPuSoftDropZ05B156PFbTagger.JetBProbabilityBJetTags
akPuSoftDropZ05B156PFSoftPFMuonByPtBJetTags = akPuSoftDropZ05B156PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags = akPuSoftDropZ05B156PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropZ05B156PFTrackCountingHighEffBJetTags = akPuSoftDropZ05B156PFbTagger.TrackCountingHighEffBJetTags
akPuSoftDropZ05B156PFTrackCountingHighPurBJetTags = akPuSoftDropZ05B156PFbTagger.TrackCountingHighPurBJetTags
akPuSoftDropZ05B156PFPatJetPartonAssociationLegacy = akPuSoftDropZ05B156PFbTagger.PatJetPartonAssociationLegacy
akPuSoftDropZ05B156PFPatJetPartonAssociationLegacy.partons = "myPartons"

akPuSoftDropZ05B156PFImpactParameterTagInfos = akPuSoftDropZ05B156PFbTagger.ImpactParameterTagInfos
akPuSoftDropZ05B156PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropZ05B156PFJetProbabilityBJetTags = akPuSoftDropZ05B156PFbTagger.JetProbabilityBJetTags

akPuSoftDropZ05B156PFSecondaryVertexTagInfos = akPuSoftDropZ05B156PFbTagger.SecondaryVertexTagInfos
akPuSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B156PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B156PFCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B156PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B156PFbTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropZ05B156PFSecondaryVertexNegativeTagInfos = akPuSoftDropZ05B156PFbTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropZ05B156PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropZ05B156PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropZ05B156PFNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B156PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropZ05B156PFPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropZ05B156PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropZ05B156PFNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B156PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropZ05B156PFPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropZ05B156PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropZ05B156PFSoftPFMuonsTagInfos = akPuSoftDropZ05B156PFbTagger.SoftPFMuonsTagInfos
akPuSoftDropZ05B156PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropZ05B156PFSoftPFMuonBJetTags = akPuSoftDropZ05B156PFbTagger.SoftPFMuonBJetTags
akPuSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags = akPuSoftDropZ05B156PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropZ05B156PFSoftPFMuonByPtBJetTags = akPuSoftDropZ05B156PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropZ05B156PFNegativeSoftPFMuonByPtBJetTags = akPuSoftDropZ05B156PFbTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropZ05B156PFPositiveSoftPFMuonByPtBJetTags = akPuSoftDropZ05B156PFbTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropZ05B156PFPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropZ05B156PFPatJetPartonAssociationLegacy*akPuSoftDropZ05B156PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akPuSoftDropZ05B156PFPatJetFlavourAssociation = akPuSoftDropZ05B156PFbTagger.PatJetFlavourAssociation
# akPuSoftDropZ05B156PFPatJetFlavourId = cms.Sequence(akPuSoftDropZ05B156PFPatJetPartons*akPuSoftDropZ05B156PFPatJetFlavourAssociation)

akPuSoftDropZ05B156PFJetBtaggingIP = cms.Sequence(
    akPuSoftDropZ05B156PFImpactParameterTagInfos *
    akPuSoftDropZ05B156PFTrackCountingHighEffBJetTags +
    akPuSoftDropZ05B156PFTrackCountingHighPurBJetTags +
    akPuSoftDropZ05B156PFJetProbabilityBJetTags +
    akPuSoftDropZ05B156PFJetBProbabilityBJetTags
    )

akPuSoftDropZ05B156PFJetBtaggingSV = cms.Sequence(
    akPuSoftDropZ05B156PFImpactParameterTagInfos *
    akPuSoftDropZ05B156PFSecondaryVertexTagInfos *
    akPuSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags +
    akPuSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags +
    akPuSoftDropZ05B156PFCombinedSecondaryVertexBJetTags +
    akPuSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags
    )

akPuSoftDropZ05B156PFJetBtaggingNegSV = cms.Sequence(
    akPuSoftDropZ05B156PFImpactParameterTagInfos *
    akPuSoftDropZ05B156PFSecondaryVertexNegativeTagInfos *
    akPuSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akPuSoftDropZ05B156PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akPuSoftDropZ05B156PFNegativeCombinedSecondaryVertexBJetTags +
    akPuSoftDropZ05B156PFPositiveCombinedSecondaryVertexBJetTags +
    akPuSoftDropZ05B156PFNegativeCombinedSecondaryVertexV2BJetTags +
    akPuSoftDropZ05B156PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akPuSoftDropZ05B156PFJetBtaggingMu = cms.Sequence(
    akPuSoftDropZ05B156PFSoftPFMuonsTagInfos *
    akPuSoftDropZ05B156PFSoftPFMuonBJetTags +
    akPuSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags +
    akPuSoftDropZ05B156PFSoftPFMuonByPtBJetTags +
    akPuSoftDropZ05B156PFNegativeSoftPFMuonByPtBJetTags +
    akPuSoftDropZ05B156PFPositiveSoftPFMuonByPtBJetTags
    )

akPuSoftDropZ05B156PFJetBtagging = cms.Sequence(
    akPuSoftDropZ05B156PFJetBtaggingIP
    * akPuSoftDropZ05B156PFJetBtaggingSV
    # * akPuSoftDropZ05B156PFJetBtaggingNegSV
    # * akPuSoftDropZ05B156PFJetBtaggingMu
    )

akPuSoftDropZ05B156PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akPuSoftDropZ05B156PFJets"),
    genJetMatch            = cms.InputTag("akPuSoftDropZ05B156PFmatch"),
    genPartonMatch         = cms.InputTag("akPuSoftDropZ05B156PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akPuSoftDropZ05B156PFcorr")),
    JetPartonMapSource     = cms.InputTag("akPuSoftDropZ05B156PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akPuSoftDropZ05B156PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akPuSoftDropZ05B156PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akPuSoftDropZ05B156PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akPuSoftDropZ05B156PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akPuSoftDropZ05B156PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akPuSoftDropZ05B156PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akPuSoftDropZ05B156PFJetBProbabilityBJetTags"),
        cms.InputTag("akPuSoftDropZ05B156PFJetProbabilityBJetTags"),
        # cms.InputTag("akPuSoftDropZ05B156PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akPuSoftDropZ05B156PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akPuSoftDropZ05B156PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akPuSoftDropZ05B156PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akPuSoftDropZ05B156PFImpactParameterTagInfos"),cms.InputTag("akPuSoftDropZ05B156PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akPuSoftDropZ05B156PFJetID"),
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

akPuSoftDropZ05B156PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akPuSoftDropZ05B156PFJets"),
    R0  = cms.double(0.6)
    )

akPuSoftDropZ05B156PFpatJetsWithBtagging.userData.userFloats.src += [
    'akPuSoftDropZ05B156PFNjettiness:tau1',
    'akPuSoftDropZ05B156PFNjettiness:tau2',
    'akPuSoftDropZ05B156PFNjettiness:tau3']

akPuSoftDropZ05B156PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akPuSoftDropZ05B156PFpatJetsWithBtagging"),
    genjetTag = 'ak6HiGenJets',
    rParam = 0.6,
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
    bTagJetName = cms.untracked.string("akPuSoftDropZ05B156PF"),
    jetName = cms.untracked.string("akPuSoftDropZ05B156PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("akSoftDropZ05B156GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("akSoftDropZ05B156HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDropZ05B156HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDropZ05B156HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("akSoftDropZ05B156GenJets","sym"),
    genDroppedBranches = cms.InputTag("akSoftDropZ05B156GenJets","droppedBranches")
    )

akPuSoftDropZ05B156PFJetSequence_mc = cms.Sequence(
    # akPuSoftDropZ05B156PFclean
    # *
    akPuSoftDropZ05B156PFmatch
    # *
    # akPuSoftDropZ05B156PFmatchGroomed
    *
    akPuSoftDropZ05B156PFparton
    *
    akPuSoftDropZ05B156PFcorr
    # *
    # akPuSoftDropZ05B156PFJetID
    *
    akPuSoftDropZ05B156PFPatJetFlavourIdLegacy
    # *
    # akPuSoftDropZ05B156PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akPuSoftDropZ05B156PFJetTracksAssociatorAtVertex
    *
    akPuSoftDropZ05B156PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akPuSoftDropZ05B156PFNjettiness
    *
    akPuSoftDropZ05B156PFpatJetsWithBtagging
    *
    akPuSoftDropZ05B156PFJetAnalyzer
    )

akPuSoftDropZ05B156PFJetSequence_data = cms.Sequence(
    akPuSoftDropZ05B156PFcorr
    *
    # akPuSoftDropZ05B156PFJetID
    # *
    akPuSoftDropZ05B156PFJetTracksAssociatorAtVertex
    *
    akPuSoftDropZ05B156PFJetBtagging
    *
    akPuSoftDropZ05B156PFNjettiness
    *
    akPuSoftDropZ05B156PFpatJetsWithBtagging
    *
    akPuSoftDropZ05B156PFJetAnalyzer
    )

akPuSoftDropZ05B156PFJetSequence_mb = cms.Sequence(
    akPuSoftDropZ05B156PFJetSequence_mc)
akPuSoftDropZ05B156PFJetSequence_jec = cms.Sequence(
    akPuSoftDropZ05B156PFJetSequence_mc)

akPuSoftDropZ05B156PFJetSequence = cms.Sequence(
    akPuSoftDropZ05B156PFJetSequence_mb)
akPuSoftDropZ05B156PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropZ05B156PFJets:sym']
akPuSoftDropZ05B156PFpatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropZ05B156PFJets:droppedBranches']
