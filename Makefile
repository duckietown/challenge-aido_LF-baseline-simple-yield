submit:
	dts challenges submit

submit-LFV_multi:
	dts challenges submit --challenge aido-LFV_multi_full-sim-validation

submit-LFVI_multi:
	dts challenges submit --challenge aido-LFVI_multi_full-sim-validation

submit-bea:
	dts challenges submit --impersonate 1639 --challenge all --retire-same-label --priority 65 --buildx

evaluate-LFV_multi:
	dts challenges evaluate --challenge aido-LFV_multi_full-sim-validation

evaluate-LFVI_multi:
	dts challenges evaluate --challenge aido-LFVI_multi_full-sim-validation
