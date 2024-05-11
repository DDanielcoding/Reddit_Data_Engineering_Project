from airflow import DAG
from datetime import datetime
import os
import sys

from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline

default_args = {
    'owner': 'D D',
    'start_date': datetime(2023, 10, 22)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)


#{'comment_limit': 2048,
# 'comment_sort': 'confidence',
# '_reddit': <praw.reddit.Reddit object at 0x7f18d9e7ca30>,
# 'approved_at_utc': None,
# 'subreddit': Subreddit(display_name='dataengineering'),
# 'selftext': 'I am working in a company where I am the only guy working on aws with a client. So alot of time I am just doing things which look good to me or I find something on internet.\n\nPlus there are not a lot of Senior Data Engineer from whom I can learn anything. I mean there are many people senior than me but its just that they are not that great. \n\nI am really trying to move to a company where I can grow with time and learn things from experience but since I am just doing bullshit work everyday for a client who will always overburden me with stuff I am just too tired to do any leetcode or sql so most of the interviews I do I fail them. and because I lack good data engineering skills.\n\nIn all this scenario how can I make a plan for 3-5 months so that I might be able to clear interviews while also learning things on the side to constantly upskill myself.', 'author_fullname': 't2_voioqmae', 'saved': False, 'mod_reason_title': None, 'gilded': 0, 'clicked': False, 'title': 'How can I upskill myself', 'link_flair_richtext': [], 'subreddit_name_prefixed': 'r/dataengineering', 'hidden': False, 'pwls': 6, 'link_flair_css_class': '', 'downs': 0, 'thumbnail_height': None, 'top_awarded_type': None, 'hide_score': False, 'name': 't3_1cpcx94', 'quarantine': False, 'link_flair_text_color': 'light', 'upvote_ratio': 0.91, 'author_flair_background_color': None, 'subreddit_type': 'public', 'ups': 26, 'total_awards_received': 0, 'media_embed': {}, 'thumbnail_width': None, 'author_flair_template_id': None, 'is_original_content': False, 'user_reports': [], 'secure_media': None, 'is_reddit_media_domain': False, 'is_meta': False, 'category': None, 'secure_media_embed': {}, 'link_flair_text': 'Career', 'can_mod_post': False, 'score': 26, 'approved_by': None, 'is_created_from_ads_ui': False, 'author_premium': False, 'thumbnail': 'self', 'edited': False, 'author_flair_css_class': None, 'author_flair_richtext': [], 'gildings': {}, 'content_categories': None, 'is_self': True, 'mod_note': None, 'created': 1715416767.0, 'link_flair_type': 'text', 'wls': 6, 'removed_by_category': None, 'banned_by': None, 'author_flair_type': 'text', 'domain': 'self.dataengineering', 'allow_live_comments': False, 'selftext_html': '<!-- SC_OFF --><div class="md"><p>I am working in a company where I am the only guy working on aws with a client. So alot of time I am just doing things which look good to me or I find something on internet.</p>\n\n<p>Plus there are not a lot of Senior Data Engineer from whom I can learn anything. I mean there are many people senior than me but its just that they are not that great. </p>\n\n<p>I am really trying to move to a company where I can grow with time and learn things from experience but since I am just doing bullshit work everyday for a client who will always overburden me with stuff I am just too tired to do any leetcode or sql so most of the interviews I do I fail them. and because I lack good data engineering skills.</p>\n\n<p>In all this scenario how can I make a plan for 3-5 months so that I might be able to clear interviews while also learning things on the side to constantly upskill myself.</p>\n</div><!-- SC_ON -->', 'likes': None, 'suggested_sort': None, 'banned_at_utc': None, 'view_count': None, 'archived': False, 'no_follow': False, 'is_crosspostable': False, 'pinned': False, 'over_18': False, 'all_awardings': [], 'awarders': [], 'media_only': False, 'link_flair_template_id': '069dd614-a7dc-11eb-8e48-0e90f49436a3', 'can_gild': False, 'spoiler': False, 'locked': False, 'author_flair_text': None, 'treatment_tags': [], 'visited': False, 'removed_by': None, 'num_reports': None, 'distinguished': None, 'subreddit_id': 't5_36en4', 'author_is_blocked': False, 'mod_reason_by': None, 'removal_reason': None, 'link_flair_background_color': '#349e48', 'id': '1cpcx94', 'is_robot_indexable': True, 'report_reasons': None, 'author': Redditor(name='pixel_pirate1'), 'discussion_type': None, 'num_comments': 8, 'send_replies': True, 'whitelist_status': 'all_ads', 'contest_mode': False, 'mod_reports': [], 'author_patreon_flair': False, 'author_flair_text_color': None, 'permalink': '/r/dataengineering/comments/1cpcx94/how_can_i_upskill_myself/', 'parent_whitelist_status': 'all_ads', 'stickied': False, 'url': 'https://www.reddit.com/r/dataengineering/comments/1cpcx94/how_can_i_upskill_myself/', 'subreddit_subscribers': 182736, 'created_utc': 1715416767.0, 'num_crossposts': 0, 'media': None, 'is_video': False, '_fetched': False, '_additional_fetch_params': {}, '_comments_by_id': {}}


#extraction from reddit
extract = PythonOperator(
    task_id = 'reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs = {
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag
)
#upload to s3
upload_s3 = PythonOperator(
    task_id = 's3_upload',
    python_callable = upload_s3_pipeline,
    dag=dag

)

extract >> upload_s3