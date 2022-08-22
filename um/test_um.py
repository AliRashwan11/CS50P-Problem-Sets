from um import count

def test_zero_ums():
    assert count("I got that yummy yummy !")==0
    assert count("mum, this is not good news")==0
    assert count("Where are we going ? ")==0

def test_one_um():
    assert count("um, yes my name is Ali")==1
    assert count("I had,um a new Idea I wanted to talk about")==1
    assert count("No um, I have nothing to say to you")==1

def test_two_ums():
    assert count("um, this is not good news,um I'm alittle shocked")==2
    assert count("mum, I wanted to um, tell you something, um..")==2


def test_case_sensitivity():
    assert count("Um, yes why not")==1


    
