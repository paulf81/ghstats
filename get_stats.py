import github_stats as ghs
import database as dbc

# This script will retrieve github stats via their API and store in a postgres database

db = dbc.Database()

# NREL/FLORIS 
traffic = ghs.RepoTraffic(owner='NREL', repository='floris')
views = traffic.get_views()
clones = traffic.get_clones()

if clones['clones']:
    db.addClones(clones['clones'],repo_code='nrel_floris')

if views['views']:
    db.addViews(views['views'],repo_code='nrel_floris')

# NREL / FLASC 
traffic = ghs.RepoTraffic(owner='NREL', repository='flasc')
views = traffic.get_views()
clones = traffic.get_clones()

if clones['clones']:
    db.addClones(clones['clones'],repo_code='nrel_flasc')

if views['views']:
    db.addViews(views['views'],repo_code='nrel_flasc')


# NREL / Hercules 
traffic = ghs.RepoTraffic(owner='NREL', repository='hercules')
views = traffic.get_views()
clones = traffic.get_clones()

if clones['clones']:
    db.addClones(clones['clones'],repo_code='nrel_hercules')

if views['views']:
    db.addViews(views['views'],repo_code='nrel_hercules')

# NREL / WHOC 
traffic = ghs.RepoTraffic(owner='NREL', repository='wind-hybrid-open-controller')
views = traffic.get_views()
clones = traffic.get_clones()

if clones['clones']:
    db.addClones(clones['clones'],repo_code='nrel_whoc')

if views['views']:
    db.addViews(views['views'],repo_code='nrel_whoc')

# NREL / moa_python 
traffic = ghs.RepoTraffic(owner='NREL', repository='moa_python')
views = traffic.get_views()
clones = traffic.get_clones()

if clones['clones']:
    db.addClones(clones['clones'],repo_code='nrel_moa_python')

if views['views']:
    db.addViews(views['views'],repo_code='nrel_moa_python')