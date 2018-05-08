
import invdbase

# dset = invdbase.invASDF('/scratch/summit/life9360/ALASKA_work/mc_inv_files/inversion_alaska.h5')
dset = invdbase.invASDF('/work3/leon/mc_inv_files/inversion_alaska.h5')
# dset = invdbase.invASDF('../../inversion_alaska.h5')
# dset.read_ref_dbase(inasdfname='/scratch/summit/life9360/ALASKA_work/ASDF_data/ref_Alaska.h5')
# dset.read_raytomo_dbase(inh5fname='/scratch/summit/life9360/ALASKA_work/hdf5_files/ray_tomo_Alaska_20180410.h5', runid=2, Tmin=8., Tmax=50.)

# dset.read_moho_depth()
# dset.read_sediment_depth()
# dset.read_CU_model()
# vpr = dset.mc_inv_iso(instafname='ref_log')
# dset.mc_inv_iso(instafname='ref_log', outdir='/scratch/summit/life9360/ALASKA_work/mc_inv_files/mc_results')

dset.mc_inv_iso_mp(instafname='ref_log', outdir='/work3/leon/mc_inv_files/mc_results_100000', nprocess=10, subsize=50, numbrun=100000)