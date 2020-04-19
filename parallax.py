from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

distance = 100  # True distance in parsecs
parallax = 1 / distance

# Fractional parallax measurement uncertainty
# f = parallax_std_deviation / parallax
f = 0.03

parallax_std_deviation = f * parallax
samples = 10000  # number of parallaxes

# Draw random samples from normal distributions around 'true' parallax
# using measurement uncertainty as stndard deviation
parallax_measured = stats.norm.rvs(loc=parallax,
                                   scale=parallax_std_deviation,
                                   size=samples)

distance_measured = 1 / parallax_measured

# Plot distribution of distances
fig, axs = plt.subplots(1, 2, sharey=True)

sns.distplot(distance_measured, kde=False, norm_hist=True,
             ax=axs[0], bins=40,
             hist_kws={
                "color": "#00a6ff",
                "zorder": 1,
                "edgecolor": "#FFFFFF",
                "linewidth": 1,
                "alpha": 1})

axs[0].axvline(x=distance, ymin=0, ymax=1, lw=2,
               color='red', linestyle="--")

# Remove ticks and tick labels
axs[0].get_yaxis().set_ticks([])
axs[1].get_yaxis().set_ticks([])

xlabel = "Distance r [pc]"
# axs[0].set_xlabel(xlabel)
# axs[1].set_xlabel(xlabel)
axs[0].set_ylabel("Number of samples")
# plt.xlabel(xlabel)
fig.text(0.5, 0.03, xlabel, va='center', ha='center')
plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()
