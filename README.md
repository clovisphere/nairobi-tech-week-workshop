# Performance Testing Workshop
Code for a presentation at the [Nairobi Tech Week](https://nairobitechweek.com/) on [Performance Testing](https://www.wikiwand.com/en/Software_performance_testing) using the :sparkles:coolest:sunglasses::sparkles: tools: [locust](https://locust.io/) and [Taurus](https://gettaurus.org/).

### Installation
You need to have [Python](https://www.python.org/) installed, [Python 3](https://www.python.org/downloads/) preferably, as well as [git](https://git-scm.com/).

1. Clone this repo, and make it your working directory.

```
git clone git@github.com:clovisphere/nairobi-tech-week-workshop.git && cd nairobi-tech-week-workshop
```

The directory should look like:

```
.
├── Locust-Presentation.pptx
├── README.md
└── perf
    ├── app.py
    ├── demo.yml
    └── requirements.txt
```

2. Using [pipenv](https://pipenv.readthedocs.io/en/latest/), [virtualenv](https://virtualenv.pypa.io/en/latest/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) create an environment, and install the required packages.

```
pip install -r perf/requirements.txt
```

:smiley::wink: enjoy:zzz::ok_hand:
