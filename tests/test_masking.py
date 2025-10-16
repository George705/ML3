from datascrub.patterns import mask_all

def test_email_mask():
    assert mask_all("reach me at john@example.com") != "reach me at john@example.com"
