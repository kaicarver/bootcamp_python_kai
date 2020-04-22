#!/usr/bin/env python

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    'Perl': 'Larry Wall',
}

print("\n".join(
                "{} was created by {}".format(k, v)
                for k, v in languages.items()))
