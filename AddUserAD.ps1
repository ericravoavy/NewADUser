#Creating PSobject model with information properties of a new employee.
#These informations should be provided by HR departement

#Import all the command module fo managing active directory
#ConnectAD.ps1
#Connect to your Domain Controller(DC)
#Change the value after the -ComputerName to your know DC

#$session = New-PSSession -ComputerName "VWSERVDCSH" -Credential (Get-Credential)
#Invoke-Command $session -Scriptblock { Import-Module ActiveDirectory }
#Import-PSSession -Session $session -module ActiveDirectory

param(
    $name,
    $given_name,
    $last_name,
    $samaccountname,
    $login,
    $Tel_Number,
    $mail_address
    #$departement,
    #$function
    )
#describe the properties of Userclass object
$Userclass = New-Object psobject -Property @{
    name = $null
    first_name = $null
    last_name = $null
    samaccountname = $null
    login = $null
    Tel_number = $null
    mail_address = $null
    departement = $null
    function = $null
    OUPath = $null
    Enable = $null
}

#Contructor of userclass class
#define the mandatory information parameters of the object
function Userclass {
    param(
        [Parameter(Mandatory=$true)]
        [String]$name,
        [Parameter(Mandatory=$true)]
        [String]$first_name,
        [Parameter(Mandatory=$true)]
        [string]$last_name,
        [parameter(Mandatory=$true)]
        [string]$samaccountname,
        [parameter(Mandatory=$true)]
        [string]$login,
        [Parameter(Mandatory=$false)]
        [long]$Tel_number,
        [Parameter(Mandatory=$false)]
        [string]$mail_address,
        [Parameter(Mandatory=$false)]
        #[ValidateSet('CA','Treasury','IT','Finance')]
        [String]$departement,
        [Parameter(Mandatory=$false)]
        #[ValidateSet('IT','Accountant','VP','AVP')]
        [string]$function,
        [Parameter(Mandatory=$false)]
        [string]$OUPath,
        [Parameter(Mandatory=$false)]
        [string]$Enable
    )
    $Userclass = $Userclass.psobject.copy()
    $Userclass.name = $name
    $Userclass.first_name = $first_name
    $Userclass.last_name = $last_name
    $Userclass.samaccountname = $samaccountname
    $Userclass.login = $login
    $Userclass.Tel_number = $Tel_number
    $Userclass.mail_address = $mail_address
    $Userclass.departement = $departement
    $Userclass.function = $Function
    $userclass.OUPath = $OUPath
    $userclass.Enable = $Enable
    $Userclass
}

echo "la class userclass définissant un utilisateur de l'AD est défini"


#Initiate an user from class Userclass
$New_User = Userclass -name $name -first_name $given_name -last_name $last_name -samaccountname $samaccountname -login $login -Tel_number $Tel_Number -mail_address $mail_address -OUPath "OU=Laptop Users,OU=Users,OU=SH,DC=silver-holdings,DC=lan" -Enable "$true"

#display the new User created
echo $New_User

New-ADUser -Name $New_User.name -GivenName $New_User.first_name -Surname $New_User.last_name -SamAccountName $samaccountname -UserPrincipalName $login -OfficePhone $New_User.Tel_number -EmailAddress $New_User.mail_address -Path $New_User.OUPath -AccountPassword (ConvertTo-SecureString "Welcome.2019" -AsPlainText -force) -PassThru -Enabled $true
