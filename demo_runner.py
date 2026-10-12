"""Deterministic offline contract replay, not a production execution engine."""
import json
from pathlib import Path


def replay(data):
    if data['classification'] != 'SYNTHETIC_DEMO_ONLY' or data['external_actions'] is not False:
        raise ValueError('Synthetic offline data only')
    if data['commercial']['owner_gate'] is not None or data['commercial']['pricing_status'] != 'unknown':
        raise ValueError('No actual approval or price in this demo')
    if any(v is not None for v in data['money'].values()):
        raise ValueError('No fake financial results')
    if data['content']['status'] != 'scripts' or data['content']['published_at'] is not None:
        raise ValueError('Campaign draft must not look published')
    if data['performance']['content_id'] != data['content']['content_id']:
        raise ValueError('Result-to-material linkage mismatch')
    if data['manual_result']['views'] != data['performance']['metrics']['views']:
        raise ValueError('Result-to-performance mismatch')
    if data['manual_result']['saves'] != data['performance']['metrics']['saves']:
        raise ValueError('Unknown/zero result mismatch')
    if data['experiment']['status'] != 'planned':
        raise ValueError('Experiment proposal only')
    baseline = data['experiment']['control_baseline']
    if baseline['content_id'] != data['content']['content_id'] or baseline['publication_id'] != data['manual_result']['publication_id']:
        raise ValueError('Learning-to-result linkage mismatch')
    metrics = data['performance']['metrics']
    unknown = lambda v: 'Unknown' if v is None else str(v)
    frames = [
        ('Owner Goal', data['goal']),
        ('External Opportunity', data['candidate']['title']+' — synthetic request, not a client; rank unknown'),
        ('Demand Analysis', 'Capability: '+data['analysis']['capability_match']['value']['overall']+
         '; eligibility: unknown, not PASS; recommendation: needs data'),
        ('Execution Plan', '; '.join(s['owner']+': '+s['title']+' ('+s['execution_status']+')' for s in data['execution_steps'])),
        ('Commercial Pack / Owner Gate', 'Needs data; price unknown; owner gate pending; draft is not sent'),
        ('MEDIA Full Loop', ' → '.join(data['media_lifecycle'])+'. Draft: scripts, not published. Manual result below is a separate synthetic illustration, not this campaign publication.'),
        ('Learning', 'SYNTHETIC views: '+unknown(metrics['views'])+'; saves: '+unknown(metrics['saves'])+
         '; confidence unknown; next experiment planned, not executed'),
        ('Money Honesty', 'Recorded cost unknown; estimated cost unknown; revenue/profit/ROI unknown. Potential is not revenue.'),
    ]
    return {'classification':'SYNTHETIC_DEMO_ONLY','external_actions':False,
            'frames':[{'step':i+1,'title':title,'summary':text} for i,(title,text) in enumerate(frames)]}


if __name__ == '__main__':
    fixture = Path(__file__).with_name('demo_fixture.json')
    print(json.dumps(replay(json.loads(fixture.read_text(encoding='utf-8'))),ensure_ascii=True,sort_keys=True,indent=2))
