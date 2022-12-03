
if __name__ == '__main__':
    from google_play_scraper import Sort, reviews_all, app

    reviews_1 = reviews_all(
        'com.gojek.app',
        sleep_milliseconds=0,  # defaults to 0
        lang='id',  # defaults to 'en'
        country='id',  # defaults to 'us'
        sort=Sort.MOST_RELEVANT,  # defaults to Sort.MOST_RELEVANT
        filter_score_with=1  # defaults to None(means all score)
    )

    print(len(reviews_1))

    reviews_2 = reviews_all(
        'com.gojek.app',
        sleep_milliseconds=0,  # defaults to 0
        lang='id',  # defaults to 'en'
        country='id',  # defaults to 'us'
        sort=Sort.MOST_RELEVANT,  # defaults to Sort.MOST_RELEVANT
        filter_score_with=2  # defaults to None(means all score)
    )

    print(len(reviews_2))

    reviews_3 = reviews_all(
        'com.gojek.app',
        sleep_milliseconds=0,  # defaults to 0
        lang='id',  # defaults to 'en'
        country='id',  # defaults to 'us'
        sort=Sort.MOST_RELEVANT,  # defaults to Sort.MOST_RELEVANT
        filter_score_with=3  # defaults to None(means all score)
    )

    print(len(reviews_3))

    reviews_4 = reviews_all(
        'com.gojek.app',
        sleep_milliseconds=0,  # defaults to 0
        lang='id',  # defaults to 'en'
        country='id',  # defaults to 'us'
        sort=Sort.MOST_RELEVANT,  # defaults to Sort.MOST_RELEVANT
        filter_score_with=4  # defaults to None(means all score)
    )

    print(len(reviews_4))

    reviews_5 = reviews_all(
        'com.gojek.app',
        sleep_milliseconds=0,  # defaults to 0
        lang='id',  # defaults to 'en'
        country='id',  # defaults to 'us'
        sort=Sort.MOST_RELEVANT,  # defaults to Sort.MOST_RELEVANT
        filter_score_with=5  # defaults to None(means all score)
    )

    print(len(reviews_5))


    # score = [0, 0, 0, 0, 0]
    #
    # for review in result:
    #     if review['score'] == 1:
    #         score[0] += 1
    #     elif review['score'] == 2:
    #         score[1] += 1
    #     elif review['score'] == 3:
    #         score[2] += 1
    #     elif review['score'] == 4:
    #         score[3] += 1
    #     else:
    #         score[4] += 1
    #
    # print(score)
