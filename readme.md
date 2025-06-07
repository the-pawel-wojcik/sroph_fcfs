# The FCF for SrOPh
Franck-Condon factors for transitions between the X-A and X-C electronic states,
that involve high excitations along the vibronically-coupling modes (fully
symmetric modes in case of the X-C couplings).

## Computational model
The model assumes the harmonic approximation for all electronic states. The
ground state's geometry is optimized using the
`ae-EOM-EA-CCSD/cc-pVDZ[H,C,O]/cc-pwCVDZ-DK2[Sr]` model (called `g0` geometry).
At the `g0` geometry the Hessian calculations using the same model produce the
harmonic frequencies and normal modes for the X states.

Using the same model and the same procedure of optimization -> Hessian
calculations but applied for the X and C states respecively produces the
remaining parameters of the model.

The model paramerts are parsed with the `ezFCF`'s `make_xml.py` script, and the
`ezFCF` program is used with its `print_franck_condon_matrices` flag set to
`true`. To shows the FCFs for very high excitations a trick is used, i.e., the
`max_vibr_excitations_in_target_el_state` is set to a very high value (60),
while the `do_not_excite_subspace` parameter is set to comprise all but one
mode.

## Results
