#ifndef YASHE__ENC___DATASET__CLASS
#define YASHE__ENC___DATASET__CLASS

/*
   Class to model a dataset to HomomorphickNN
*/

#include "EncryptedDataInstance.h"
#include "DataInstance.h"
#include "Dataset.h"

#include "lib/ope/lib/ope.hh"
#include "lib/yashe/src/Yashe.h"
#include "lib/yashe/src/CoefficientwiseCRT.h"

#include <vector>
#include <iostream>

#include <NTL/ZZ.h>

class EncryptedDataset {
    
	private:
	OPE& ope;
	Yashe& yashe;
	const CoefficientwiseCRT& crt;
	unsigned int number_of_classes;

	vector<NTL::ZZ> encrypt_vector(const DataInstance& sample);
	RealNumberPlaintext encode_class(unsigned int class_id);
	EncryptedDataInstance encrypt_training_instance(const DataInstance& sample);
	void encrypt_training_data(vector<DataInstance> data);
	void encrypt_testing_data(vector<DataInstance> data);

    public:
	std::vector<EncryptedDataInstance> training_data; // Data instances whose classes are already know
	std::vector<EncryptedDataInstance> testing_data; // Data instances used to verify the accuracy of the classifier

	EncryptedDataset(const Dataset& plain_dataset, OPE& ope, Yashe& yashe, CoefficientwiseCRT& crt);

	unsigned int number_of_training_instances();
	unsigned int number_of_testing_instances();

	unsigned int instances_dimensions();
};

std::ostream& operator<<(std::ostream&, const EncryptedDataset&);

#endif