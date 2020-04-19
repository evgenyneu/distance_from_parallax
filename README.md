# Calculating distances from uncertain parallax measurements

This is a Python program that plots measured stellar distances from simulated parallaxes. The plot demonstrates that one can not just use the standard distance = 1/parallax formula when parallax
measurements are uncertain or negative, which is true for most stars in Gaia's DR2 catalog. Instead, the parallaxes need to be inferred using statistical inference.

This is a recreation of Figure 3 in [Luri X et. al (2018)](https://arxiv.org/abs/1804.09376).
