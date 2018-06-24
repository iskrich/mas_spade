import spade

def propose_template():
    propose_template = spade.Behaviour.ACLTemplate()
    propose_template.setPerformative('cfp')
    return propose_template


def bid_template():
    bit_template = spade.Behaviour.ACLTemplate()
    bit_template.setPerformative('inform')
    return bit_template


PROPOSAL_TEMPLATE = propose_template()
BID_TEMPLATE = bid_template()
