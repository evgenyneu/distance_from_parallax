"""
This is a Python program that plots stellar distances from
simulated parallaxes that have measurement uncertainties.
"""

from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns


def plot_distance(ax, distance, f, samples, xlim, bins=40):
    """
    Plot distances from observed parallaxes.

    Parameters
    ---------
    ax: Matplotlib's axis object

    distance: float
        True distance in parsecs.

    f: float
        Fractional parallax measurement uncertainty:
            f = parallax_std_deviation / parallax

    samples: int
        Number of simulated parallax measurements.

    bins: int
        Number of bins in the histogram.

    xlim: (float, float)
        A tuple containing the lower and upper limit for the x axis.
    """

    # True distance in parsecs
    parallax = 1 / distance
    parallax_std_deviation = f * parallax

    # Draw random samples from normal distributions around 'true' parallax
    # using measurement uncertainty as stndard deviation
    parallax_measured = stats.norm.rvs(loc=parallax,
                                       scale=parallax_std_deviation,
                                       size=samples)

    # Calculate distances from parallaxes using the standard equation
    distance_measured = 1 / parallax_measured

    # Exclude distances that are beyond the x-axis limits
    distance_measured = distance_measured[(distance_measured > xlim[0]) &
                                          (distance_measured < xlim[1])]

    # Show histogram of distances
    sns.distplot(distance_measured, kde=False, norm_hist=True,
                 ax=ax, bins=bins,
                 hist_kws={
                    "color": "#00a6ff",
                    "zorder": 1,
                    "edgecolor": "#FFFFFF",
                    "linewidth": 1,
                    "alpha": 1})

    # Draw vertical line for true distances
    ax.axvline(x=distance, ymin=0, ymax=1, lw=2,
               color='red', linestyle="--")

    # Remove ticks and tick labels
    ax.get_yaxis().set_ticks([])

    # Set x-axis limits
    ax.set_xlim(xlim)

    # Show the fractional uncertainty of the parallax measurement
    ax.text(0.95, 0.90, f'f={f}',
            horizontalalignment='right',
            transform=ax.transAxes)


def make_plot(file_name):
    """
    Plot distribution of distances.

    Parameters
    ---------

    file_name: str
        Name of plot file that will be created.
    """

    fig, axs = plt.subplots(1, 2, sharey=False, figsize=[6, 3])

    plot_distance(ax=axs[0], distance=100, f=0.03, samples=100000,
                  xlim=[85, 115])

    plot_distance(ax=axs[1], distance=2000, f=0.6, samples=100000,
                  xlim=[0, 5000])

    # Label the axes
    axs[0].set_ylabel("Number of samples")
    fig.text(0.5, 0.03, "Distance r [pc]", va='center', ha='center')
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    fig.savefig(fname=file_name, dpi=600)


if __name__ == '__main__':
    make_plot(file_name="measured_distances.pdf")
    print("We are done")
